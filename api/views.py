from django.shortcuts import get_object_or_404
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError
from api.models import User, Powtoon, PermissionGroup


# This route creates a user and stores it in the database
# It takes three parameters via POST: name, email and group,
# with group being an optional parameter. group is the id
# of the permission group that this user has access to.
@csrf_exempt
def user_create(request):
    group_id = request.POST.get('group')

    try:
        newuser = User(
            name=request.POST['name'],
            email=request.POST['email'],
        )

        if group_id is None:
            # By default, it has been defined in the fixture
            # that the permission group with pk = 1 is the default group
            # It's not a recommended solution, but it's simple.
            permission = get_object_or_404(PermissionGroup, pk=1)
            newuser.group = permission
        else:
            # If a group is defined, it will be
            # added to the user (if the group exists)
            permission = get_object_or_404(PermissionGroup, pk=group_id)
            newuser.group = permission

        newuser.save()
    except KeyError:
        return JsonResponse({
            'error': 'All fields need to be filled.'
        })
    except IntegrityError:
        return JsonResponse({
            'error': 'The email entered is already registered'
        })

    response = serialize('json', [newuser])
    return HttpResponse(response, content_type='application/json')


# This route displays all registered users
# Only admin users have access to it.
#
# This route takes a parameter in the URL: user_id
# user_id is the id of the user who is accessing
# Example: /read/4
def user_read(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    # By default, it has been defined in the fixture
    # that the permission group with pk = 2 is the
    # group with administrator permissions.
    # It's not a recommended solution, but it's simple.
    admingroup = get_object_or_404(PermissionGroup, pk=2)

    if user.group.id != admingroup.id:
        return JsonResponse({
            'error': 'You are not allowed for this.'
        })

    users = User.objects.all()
    response = serialize('json', users)
    return HttpResponse(response, content_type='application/json')


# This route creates a powtoon
# It takes three parameters via POST: name, content and owner_id.
# Content must be a valid JSON, and owner_id an id of a
# registered user.
@csrf_exempt
def powtoon_create(request):
    try:
        newpowtoon = Powtoon(
            name=request.POST['name'],
            content=request.POST['content'],
            owner_id=request.POST['owner_id'],
        )

        newpowtoon.save()
    except KeyError:
        return JsonResponse({
            'error': 'All fields need to be filled.'
        })

    response = serialize('json', [newpowtoon])
    return HttpResponse(response, content_type='application/json')


# This route edits a powtoon
# You can only edit a powtoon if you own it or if you are
# in the admin group
#
# It takes two parameters in the URL: user_id and powtoon_id.
# user_id is the id of the user who is accessing
# powtoon_id is the id of the powtoon that will be edited
# Example: edit/5/3
@csrf_exempt
def powtoon_edit(request, user_id, powtoon_id):
    user = get_object_or_404(User, pk=user_id)
    currentpowtoon = Powtoon.objects.filter(pk=powtoon_id)
    powton = currentpowtoon.first()

    if len(currentpowtoon) == 0:
        return JsonResponse({
            'error': 'Powtoon not found'
        })

    # Only powtoon owner can edit it
    if powton.owner_id != user.id:
        return JsonResponse({
            'error': 'You are not allowed for this.'
        })

    newname = request.POST.get('name')
    newcontent = request.POST.get('content')

    # Editing the value of attributes only if
    # they were specified in the request body
    if newname is not None:
        currentpowtoon.update(name=newname)

    if newcontent is not None:
        currentpowtoon.update(content=newcontent)

    return JsonResponse({
        'message': 'Successfully updated',
    })


# This route displays all powtons
# Only administrators can access it.
#
# This route takes a parameter in the URL: user_id
# user_id is the id of the user who is accessing
# Example: /read/5
@csrf_exempt
def powtoon_read(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    # By default, it has been defined in the fixture
    # that the permission group with pk = 2 is the
    # group with administrator permissions.
    # It's not a recommended solution, but it's simple.
    admingroup = get_object_or_404(PermissionGroup, pk=2)
    powtoons = Powtoon.objects.all()

    if user.group.id != admingroup.id:
        return JsonResponse({
            'error': 'You are not allowed for this.'
        })

    response = serialize('json', powtoons)
    return HttpResponse(response, content_type='application/json')


# This route displays a powtoon
# You can only see a powtoon if you own it,
# or if you are in the admin group
#
# This route takes two parameters in the URL: user_id and powtoon_id
# user_id is the id of the user who is accessing
# powtoon_id is the id of the powtoon that will be accessed
# Example: /find/4/2
def powtoon_find_by_id(request, user_id, powtoon_id):
    user = get_object_or_404(User, pk=user_id)
    # By default, it has been defined in the fixture
    # that the permission group with pk = 2 is the
    # group with administrator permissions.
    # It's not a recommended solution, but it's simple.
    admingroup = get_object_or_404(PermissionGroup, pk=2)

    powtoon = get_object_or_404(Powtoon, pk=powtoon_id)
    response = serialize('json', [powtoon])

    if (powtoon.owner_id != user.id) and (user.group.id != admingroup.id):
        return JsonResponse({
            'error': 'You are not allowed for this.'
        })

    return HttpResponse(response, content_type='application/json')


# This route deletes a powtoon
# This route takes two parameters: user_id and powtoon_id.
# You can only delete a powtoon if you own it,
# or an administrator
#
# This route takes two parameters in the URL: user_id and powtoon_id
# user_id is the id of the user who is accessing
# powtoon_id is the id of the powtoon that will be deleted
# Example: /find/5/3
def powtoon_delete(request, user_id, powtoon_id):
    user = get_object_or_404(User, pk=user_id)
    powtoon = get_object_or_404(Powtoon, pk=powtoon_id)
    powtoon.delete()

    if powtoon.owner_id != user.id:
        return JsonResponse({
            'error': 'You are not allowed for this.'
        })

    return JsonResponse({
        'message': 'Successfully deleted',
    })


# This route displays all powtoons belonging to you.
#
# This route takes a parameter in the URL: user_id
# Example: /my/4
@csrf_exempt
def powtoon_owned_by_a_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    powtoons = Powtoon.objects.filter(owner_id=user.id)
    response = serialize('json', powtoons)
    return HttpResponse(response, content_type='application/json')


# This route will show all powtoons shared with you
#
# This route takes a parameter in the URL: user_id
# user_id is the id of the user who is accessing
# Example: /shared_with_me/3
@csrf_exempt
def powtoon_shared_to_a_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    powtoons = Powtoon.objects.filter(shared_with__id=user.id)

    response = serialize('json', powtoons)
    return HttpResponse(response, content_type='application/json')


# This route shares a powton
# This route takes three POST parameters: user_id, receiver_id and powtoon_id.
# user_id must be an owner or administrator to be able to share powtoon_id.
# receiver_id is the user who will receive access to powtoon
@csrf_exempt
def powtoon_share(request):
    try:
        user_id = request.POST['user_id']
        receiver_id = request.POST['receiver_id']
        powtoon_id = request.POST['powtoon_id']
    except KeyError:
        return JsonResponse({
            'error': 'All fields need to be filled.'
        })

    user = get_object_or_404(User, pk=user_id)
    receiver_user = get_object_or_404(User, pk=receiver_id)
    powtoon = get_object_or_404(Powtoon, pk=powtoon_id)
    # By default, it has been defined in the fixture
    # that the permission group with pk = 2 is the
    # group with administrator permissions.
    # It's not a recommended solution, but it's simple.
    admingroup = get_object_or_404(PermissionGroup, pk=2)

    if (powtoon.owner_id != user.id) and (user.group.id != admingroup.id):
        return JsonResponse({
            'message': 'This powtoon does not belong to you',
        })

    powtoon.shared_with.add(receiver_user)
    return JsonResponse({
        'message': 'Successfully shared',
    })
