Required instalation:
sudo apt-get install python3-mysqldb
sudo apt-get install python3-dev
sudo apt-get install python3-dev libmysqlclient-dev
pip3 install mysqlclient

pip3 install django=1.11

pip3 install djangorestframework
pip3 install markdown   
pip3 install django-filter


1) create a database named 'dash' in mysql from terminal (normal way)
2) if you have any updates in mysql db updates like password or username
go to src/dash_project/dash_project/settings.py go to database section .
example :

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD':'',
        'NAME':'dash',
        'host':'localhost',
        'port':'3306',
    }
}

- Migrate the databse 
  cd src/dash_app  python3 manage.py makemigrations
                   python3 manage.py migrate
                   python3 manage.py runserver





- now your data base is empty.
  you can add company name and net worth in data base :
    frist you got admin page  127.0.0.1:8000/admin
    username : shafa909
    password : qwerty

- open company table and, add some company and net-worth value.
  
- you can run page  127.0.0.1:8000/home

more about sql and orm :

Please read this :https://docs.djangoproject.com/en/1.11/topics/db/models/
                  
                  https://docs.djangoproject.com/en/1.11/topics/db/sql/












