# Installation

Installation is easy, you don't  really have to do much.

## Using a virtual environment to install dependencies

Using the `venv` module that is now part of the standard library (python 3.3+).

### For Windows

```sh
# creating the virtual env
$ python3 -m venv <your_env_dir>
# activating the environment
$ venv\scripts\activate
```

## Installing dependencies

```sh
$ pip install -r requirements.txt
```

Add `'rest_framework'` to your `INSTALLED_APPS` setting.

    INSTALLED_APPS = [
        ...
	    'api.apps.ApiConfig',
	    'rest_framework',
	    'drf_yasg',
    ]


# Db migration

The configured database is sqlite (just for demonstration purposes)

```sh
$ python manage.py migrate
# create an administrator account
$ python manage.py createsuperuser --email admin@example.com --username admin
```

# Run the tests

```sh
$ python manage.py test
```

# Run the app

```sh
$ python manage.py runserver
```


# Site URLs
This project is using the Django's REST framework api view, so it has also an html ui at `localhost:8000/api`.

Admin site: `http://localhost:8000/admin`

API: `http://localhost:8000/api/`

API docs: `http://localhost:8000/swagger/`


# Overview
This is a RESTAPI in Python with Django for managing user's data. 

## Endpoints
The application has the following endpoints:

```sh
/api/users - GET - To list the users
/api/users - POST - To create a new user
/api/users/{id} - GET - To get the details of a user
/api/users/{id} - PUT - To update the details of a user
/api/users/{id} - DELETE - To delete the user
```
It also supports some query parameters:-
```sh
i. page - a number for pagination
ii. limit - no. of items to be returned, default limit is 5
iii. name - search user by name as a substring in First Name or Last Name (Note, use substring
matching algorithm/pattern to match the name). It should be case-insensitive.
iv. Sort - name of attribute, the items to be sorted. 
```
**Sample query endpoint:**

```sh
/api/users?page=1&limit=10&name=James&sort=-age
```
This endpoint will return list of 10 users whose first name or last name contains substring given name and sort the users by age in descending order of page 1.

The link to the live App for testing purposes, available here - [http://datapeace.herokuapp.com/][docs].

**Below**: *Screenshot from the browsable API*
![ScreenShot](https://i.postimg.cc/52Y2FhS0/Api-Overview-Django-REST-framework.png)

![ScreenShot](https://i.postimg.cc/9fyXLySH/Users-List-Django-REST-framework-1.png)

![ScreenShot](https://i.postimg.cc/t4KCdBBz/Data-Peace.png)

# Contributors
```json
{
  "Oyebami Festus":{
    "repository": "https://github.com/Festorah/django-rest",
    "email":"festusoyebami@gmail.com"
  }
}
```

## License

Copyright © Oyebami Festus. Licensed under the [Apache License](/LICENSE).
