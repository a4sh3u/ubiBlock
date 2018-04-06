
# Models - Creating db structure
 - Init the db with django tables    
    `python manage.py migrate`
 - Make migration : Validate the model and create the migration file in migrations directory    
    `python manage.py makemigrations backend` 
 - View the SQL file    
    `python manage.py sqlmigrate backend 0001`
 - ACHTUNG : Table creation     
    `python manage.py migrate`
    
    
# Creating Admin User
  `python manage.py createsuperuser`
  
# Strating Development Server
  `python manage.py runserver`
  
