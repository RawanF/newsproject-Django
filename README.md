# News website (Python Django)
### a web application built with Django for listing the news 


A web application built with Django for displaying a list of news to users. users can signup, login, browse articles, and add them to their favorite list.



## Features

- Registration system. 
- Users can browse the articles either when logged in or as guests 
- Registered user can view, add, and remove articles from their favorite list.



## Techical stack

some technology used this project 
- [python.3.7.6]
- [Django.3.2.15]
- [Bootstrap 4]
- [Crispy forms]
- [Django generic views]

## Installation


To install and run the app follow the below commands and make sure you have created and activated a virtual environment.

Run the below command to install the requirements:
```sh
pip install -r requirements.txt
```
Execute the below command to run the application:
```sh
python3 manage.py runserver
```

The file `db.sqlite3` already contains loaded data for the articles from an external API but in case the data is deleted you can run the below command which will load the data to the local database and run the application.

```sh
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
python3 manage.py populate_db
```



**Enjoy!**



[python.3.7.6]: <https://www.python.org/downloads/release/python-376/>
   [Django.3.2.15]: <https://docs.djangoproject.com/en/3.2/>
   [Bootstrap 4]: <https://getbootstrap.com/docs/4.0/getting-started/introduction/>
   [Crispy forms]: <https://django-crispy-forms.readthedocs.io/en/latest/>
   [Django generic views]: <https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-display/>
   
