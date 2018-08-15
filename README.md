# DJANGO REST API YUMMY RECIPES

[![CircleCI](https://circleci.com/gh/PatrickCmd/django-rest-api-yummy-recipes/tree/develop.svg?style=svg)](https://circleci.com/gh/PatrickCmd/django-rest-api-yummy-recipes/tree/develop)
[![Coverage Status](https://coveralls.io/repos/github/PatrickCmd/django-rest-api-yummy-recipes/badge.svg?branch=develop)](https://coveralls.io/github/PatrickCmd/django-rest-api-yummy-recipes?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/6ae0fd096be1b2118fe0/maintainability)](https://codeclimate.com/github/PatrickCmd/django-rest-api-yummy-recipes/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/6ae0fd096be1b2118fe0/test_coverage)](https://codeclimate.com/github/PatrickCmd/django-rest-api-yummy-recipes/test_coverage)

 The innovative -----yummy recipes app----- is an application that  -----allows users  to create, save and share ----- meeting the needs of -----keeping track of awesome food recipes-----.

## TECHNOLOGIES USED
- **Python3.6**: [Python](https://www.python.org/) is a programming language that lets you work quickly and integrate systems more effectively
- **Django 1.11**: [Django](https://docs.djangoproject.com/en/1.11/) is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- **Django REST framework**: [Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs
- **Django REST framework JWT**: [Django REST framework JWT](http://getblimp.github.io/django-rest-framework-jwt/) This package provides JSON Web Token Authentication support for Django REST framework.
- **Django REST Swagger**: [Django REST Swagger](https://github.com/marcgibbons/django-rest-swagger) An API documentation generator for Swagger UI and Django REST Framework.
- **Postgresql**: [PostgreSQL](https://www.postgresql.org/) is a powerful, open source object-relational database system.
- **Pipenv**: [Pipenv](https://docs.pipenv.org/) is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world.
- **Psycopg2**: [Psycopg](http://initd.org/psycopg/) is the most popular PostgreSQL adapter for the Python programming language.

## SETTING UP THE PROJECT

### Clone the project
```
$ git clone https://github.com/PatrickCmd/django-rest-api-yummy-recipes.git
$ cd django-rest-api-yummy-recipes
```

### Active the virtual environment
```
$ pip install pipenv
$ pipenv shell
```

### Install the requirements
```
$ pipenv install
```

## SETTING UP THE DATABASE
Execute the commands in the terminal/console as stated below

### ON WINDOWS
Follow the [Link](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) on how to download 
and install postgres(>=10) on windows platform

**Create Database**
```
$ psql -U postgres
$postgres# CREATE DATABASE {dbname};  Where dbname is the database name
```
**Setup Database URL environment variable**
```
$ SET DB=postgres
$ SET DATABASE_URL=postgresql://postgres@localhost:{port}/{dbname} Where port is the port number for the postgres instance
```

### ON MAC/UBUNTU
**Install postgres**

**MAC Users**
```
$ brew install postgres
```
Follow the [link](https://brew.sh/) on how to setup brew if not yet installed

**Ubuntu users**

Follow the [Link](https://www.postgresql.org/download/linux/ubuntu/) on how to setup 
and install postgres(>=10) on Ubuntu-linux platform

**Create Database**
```
$ psql -U postgres
$ postgres# CREATE DATABASE {dbname};  Where dbname is the database name
```
**Setup Database URL environment variable**
```
$ export DB=postgres
$ export DATABASE_URL=postgresql://postgres@localhost:{port}/{dbname} Where port is the port number for the postgres instance
```

## Run the server
```
$ python manage.py runserver_plus
```
Execute the url **localhost:8000/api** in your browser

## Run tests
Execute this command at the terminal
```
$ python manage.py test
```
## Functionality(endpoints)
Endpoint | Functionality| Access
------------ | ------------- | ------------- 
POST /auth/users/register | Registers a user | PUBLIC
POST /auth/users/login |Logs a user in | PUBLIC
GET /auth/users |List registered users| PUBLIC
POST /api/categories | Creates a new recipe category | PRIVATE
GET /api/categories | Lists all created recipe categories | PRIVATE
GET /api/categories/{id} | Gets a single recipe category with the suppled id | PRIVATE
PUT /api/categories/{id} | Updates recipe category with the suppled id | PRIVATE
DELETE /api/categories/{id} | Deletes recipe_category with the suppled id | PRIVATE
POST /api/recipes | Creates a new recipe | PRIVATE
GET /api/recipes | List all recipes | PRIVATE
PUT /api/recipes/{id}| Updates a recipe item | PRIVATE
DELETE /api/recipes/{id} | Deletes arecipe in a recipe category | PRIVATE
GET /api/categories/{category_pk}/recipes | GET recipes in a category | PRIVATE
POST /api/categories/{category_pk}/recipes | Create recipes in a category | PRIVATE
GET /api/categories/{category_pk}/recipes/{id} | GET single recipe in a category | PRIVATE
PUT /api/categories/{category_pk}/recipes/{id} | Update a recipe in a recipe category | PRIVATE
DELETE /api/categories/{category_pk}/recipes/{id} | Deletes a recipe in a recipe category | PRIVATE
GET /api/public-recipes/ | GET public recipes | PUBLIC
GET /api/public-recipes/{id} | GET a single public recipe | PUBLIC
GET /api/public-recipes/{id}/reviews | GET posted reviews for a single public recipe | PUBLIC
POST /api/public-recipes/{id}/reviews | Created a review for a single public recipe | PUBLIC
GET /api/public-recipes/{id}/upvotes | GET upvotes for a single public recipe | PUBLIC
POST /api/public-recipes/{id}/upotes | Up-vote for a single public recipe | PRIVATE

## Documentation
Visit the links below for the API documentation

[CoreApi Documentation](https://django-yummy-recipes.herokuapp.com/docs/)

[Swagger Documentation](https://django-yummy-recipes.herokuapp.com/api_docs/) Login with **username:** normaluser
**password:** normaluser1234 for complete swagger-docs

[API Schema](https://django-yummy-recipes.herokuapp.com/schema/)

## Live API
Vist this [Link](https://django-yummy-recipes.herokuapp.com/api/) for the live application.