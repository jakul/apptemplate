.. include:: global.rst

Installation
============

For deployment
--------------
You must add OnPI as a source of packages ::

    $ cat ~/.pip/pip.conf
    [global]
    extra-index-url = http://newbuildbot.phase1.onzo.com/onpi/simple

You must list '|project|' as a dependency in the project requirements of the project you are deploying |project| into.

For development
---------------
 
1. Clone source code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Onzo source code is held in a Mercurial repo, hosted on the Trac server. To connect, generate an SSH key and email it to IT-Ops.

  .. parsed-literal::

     $ hg clone ssh://hg@trac.onzo.com/|project|/


2. Install source code into an existing virtualenv
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Installing the source code will make it exist on the Python path (so that it can be imported) and install any dependencies defined in the :download:`setup.py <../setup.py>` file. Use the virtualenv of the webserver you're going to be hosting |project| in.

  .. parsed-literal::

     $ workon my_venv
     $ pip install -e /path/to/|project|/
 

    
3. Import app to existing Django project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Edit the `settings.py` file of an existing Django app, and add |project| to `INSTALLED_APPS`.

  .. parsed-literal::

     INSTALLED_APPS = (
          ...
          '|project|',
          ...
      )
