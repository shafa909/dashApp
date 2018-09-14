Required instalation:
sudo apt-get install python3-mysqldb
sudo apt-get install python3-dev
sudo apt-get install python3-dev libmysqlclient-dev
pip3 install mysqlclient

pip3 install django=1.11

pip3 install djangorestframework
pip3 install markdown   
pip3 install django-filter


create a database named 'dash' in mysql from terminal (normal way)
if you have any updates in mysql db updates like password or username
go to src/dash_project/dash_project/settings.py go to database section .

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





