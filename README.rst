mobible-backend
===============

Django based backend for mobible_

Git
~~~

We're using git flow

::

    git checkout -b master
    git flow init

Just use all the defaults.


Django
~~~~~~

The requirements are in requirements.pip

::

    $ virtualenv ve
    $ source ve/bin/activate
    (ve)$ pip install -r requirements.pip
    ...// snip // ...
    (ve)$ cd webapp
    (ve)$ ./manage.py syncdb --migrate
    (ve)$ ./manage.py runserver

Point your browser at http://localhost:8000


.. _mobible: http://github.com/gsvr/mobible/