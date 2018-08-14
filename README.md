# django-rest-api-yummy-recipes

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
$postgres# CREATE DATABASE {dbname};  Where dbname is the database name
```
**Setup Database URL environment variable**
```
$ export DB=postgres
$ export DATABASE_URL=postgresql://postgres@localhost:{port}/{dbname} Where port is the port number for the postgres instance
```