Create project folder
1. create virtual environment
python -m venv ll_env
2. Activate virtual environment
ll_env\Scripts\activate
3. Install Django
pip install Django
4. Creating project 
django-admin.py startproject learning_log .
5. creating DB
python manage.py migrate
6. Viewing the project
python manage.py runserver
(see http://127.0.0.1:8000/)
7. Starting an App
python manage.py startapp learning_logs
8. Defining Models
9. Activating App
add into settings.py file INSTALLED_APPS
10. Modify the DB with new Model
python manage.py makemigrations learning_logs
11. Migrate DB
python manage.py migrate
12. create super user
python manage.py createsuperuser
13. Add data 
Go to http://localhost:8000/admin/