# Step by step commands

1. create a new project

    django-admin startproject WeightMgt

2. change to project forlder

    cd .\WeightMgt\

3. add three project applications

    python manage.py startapp user
    
    python manage.py startapp daily
    
    python manage.py startapp reports

4. register app on settings.py -> INSTALLED_APPS

5. create models on models.py in each folder

6. create/update sqlite db

    python manage.py makemigrations
    
    python manage.py migrate
