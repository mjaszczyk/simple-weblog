Simple Weblog based on Django Framework
============================================================

It is a very simple weblog build using available framework features and 
community apps.

Basic Installation
-------------------------------------------------------

[Download](https://github.com/mjaszczyk/simple-weblog/downloads) or clone
    
    git clone git@github.com:mjaszczyk/simple-weblog.git

Install requirements
    
    pip install -r requirements.txt

Prepare database

    ./manage.py syncdb --migrate

Runserver

    ./manage.py runserver

Go to [localhost:8000](http://localhost:8000/)

Tests
-------------------------------------------------------

There are few automated tests.
Run
    
    ./manage.py tests posts

Usage
-------------------------------------------------------

Admin Panel
    
    /admin/

Files Panel

    /admin/files/

Dependencies
-------------------------------------------------------

* Django 1.4
* [South](http://south.aeracode.org/)
* [Django Tagging](http://code.google.com/p/django-tagging/)
* [Django Markup](https://github.com/bartTC/django-markup)
* [Django BFM](https://github.com/simukis/django-bfm)
* [Django AutoFixture](https://github.com/gregmuellegger/django-autofixture)
* Markdown
