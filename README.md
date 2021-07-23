Powtoon task
==

#### Reminder: To start using this small project, please configure your database in powtoon/settings.py. In this project I used mysql (whose driver is specified in requiments.txt), if you use a different DBMS, please install the driver and specify in settings.py

### About apps
- User:
This app is responsible for API authentication.
  The API was implemented for use with JWT, so this app generates
  a valid token that will be used in all apps.
  
- Powtoon:
This app contains the representation of a powtoon,
  in addition to being responsible for containing all direct
  interactions with it (such as insertion, editing, deletion, queries).
  
- Share:
This app contains the representation of a permission and a group,
  and is thus responsible for determining the permissions for a user.


### How to apply fixtures?:
```
python manage.py loaddata permission
python manage.py loaddata group
```

### About routes

To learn more about routes, see the documentation on the swagger through the /swagger/ route

### About tests

To run the tests, run the User.tests.test_register test first.

Some tests like Powtoon.tests.test_share need a second registered user.

Enjoy :)
