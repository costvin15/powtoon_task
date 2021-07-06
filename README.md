Powtoon task
==

To start using this small project, please configure your database in powtoon/settings.py

In this project I used mysql (whose driver is specified in requiments.txt), if you use a different DBMS, please install the driver and specify in settings.py

After applying the migration, remember to apply the fixtures:
```
python manage.py loaddata permissions
python manage.py loaddata permissiongroup
```

Enjoy :)

For more comments, visit api/views.py
