.. include:: global.rst

Usage
=====

Adding Dependencies
-------------------

Dependencies on PyPi
^^^^^^^^^^^^^^^^^^^^
Dependencies available on PyPi simply need to be listed in *requirements.txt*::

    django

Alternatively, you can also specify the required version::

    django>=1.3

Dependencies not on PyPi
^^^^^^^^^^^^^^^^^^^^^^^^
Dependencies which are not available on PyPi should be listed both in *requirements.txt* 
(see above) and in the *dependency_links* list of *setup.py*.  The url provided in the
*dependency_links* **must include the project name and version number**::

    dependency_links = [
        'http://github.com/jakul/python-semver/tarball#egg=semver-0.0.1',
        ...
    ]

If downloading from github you may also want to specifiy the desired commit number::

    dependency_links = [
        'http://github.com/jakul/python-semver/tarball/857113414bce#egg=semver-0.0.1',
        ...
    ]

Running Tests
-------------

The tests in the test package can be performed using the test runner in runtests.py.  
The standard sytax for running PyUnit tests can be used

.. parsed-literal::

    # Ensure the environment the application has been installed into has been activated.
    
    $ python runtests.py
    
    $ python runtests.py |project|
    
    $ python runtests.py |project|.TestCase
    
    $ python runtests.py |project|.TestCase.test_method
    
Uploading to OnPI
-----------------

Add OnPI as an index server
^^^^^^^^^^^^^^^^^^^^^^^^^^^

 .. parsed-literal::
 
    $ cat ~/.pypirc
    [distutils]
    index-servers =
        onpi

    [onpi]
    repository: http://newbuildbot.phase1.onzo.com/onpi/pypi/  # The closing slash is vital
    username: craig.blaszczyk
    password: PASSWORD

Check you can connect to OnPI:

 .. parsed-literal::
    $ workon |project|
    (|project|)$ python setup.py register -r onpi
    running register
    running egg_info
    writing requirements to |project|.egg-info/requires.txt
    writing |project|.egg-info/PKG-INFO
    writing top-level names to |project|.egg-info/top_level.txt
    writing dependency_links to |project|.egg-info/dependency_links.txt
    reading manifest file '|project|.egg-info/SOURCES.txt'
    writing manifest file '|project|.egg-info/SOURCES.txt'
    warning: register: missing required meta-data: url
    Registering |project| to http://newbuildbot.phase1.onzo.com/onpi/pypi/
    Server response (200): OK
    
Any errors here will need to be fixed before you can register or upload packages to OnPi
 
Upload new release to OnPi
^^^^^^^^^^^^^^^^^^^^^^^^^^ 
#. Update the |project| metadata

    .. parsed-literal::
       $ echo "0.1.1" > |project|/version.txt
       $ echo "0.1.1\n Made some changes" >> CHANGELOG.rst

#. Build a distribution and upload it

    .. parsed-literal::
        $ workon |project|
        (|project|)$ $ python setup.py sdist upload -r onpi
        running sdist
        running egg_info
        writing requirements to |project|.egg-info/requires.txt
        writing |project|.egg-info/PKG-INFO
        writing top-level names to |project|.egg-info/top_level.txt
        writing dependency_links to |project|.egg-info/dependency_links.txt
        reading manifest file '|project|.egg-info/SOURCES.txt'
        writing manifest file '|project|.egg-info/SOURCES.txt'
        warning: sdist: standard file not found: should have one of README, README.txt
        warning: sdist: missing required meta-data: url
        creating |project|-0.1.1
        creating |project|-0.1.1/|project|
        creating |project|-0.1.1/|project|.egg-info
        creating |project|-0.1.1/|project|/tests
        making hard links in |project|-0.1.1...
        hard linking setup.py -> |project|-0.1.1
        hard linking |project|/__init__.py -> |project|-0.1.1/|project|
        hard linking |project|/models.py -> |project|-0.1.1/|project|
        hard linking |project|/urls.py -> |project|-0.1.1/|project|
        hard linking |project|/views.py -> |project|-0.1.1/|project|
        hard linking |project|.egg-info/PKG-INFO -> |project|-0.1.1/|project|.egg-info
        hard linking |project|.egg-info/SOURCES.txt -> |project|-0.1.1/|project|.egg-info
        hard linking |project|.egg-info/dependency_links.txt -> |project|-0.1.1/|project|.egg-info
        hard linking |project|.egg-info/requires.txt -> |project|-0.1.1/|project|.egg-info
        hard linking |project|.egg-info/top_level.txt -> |project|-0.1.1/|project|.egg-info
        hard linking |project|/tests/__init__.py -> |project|-0.1.1/|project|/tests
        hard linking |project|/tests/models.py -> |project|-0.1.1/|project|/tests
        hard linking |project|/tests/urls.py -> |project|-0.1.1/|project|/tests
        hard linking |project|/tests/views.py -> |project|-0.1.1/|project|/tests
        Writing |project|-0.1.1/setup.cfg
        tar -cf dist/|project|-0.1.1.tar |project|-0.1.1
        gzip -f9 dist/|project|-0.1.1.tar
        removing '|project|-0.1.1' (and everything under it)
        running upload
        Submitting dist/|project|-0.1.1.tar.gz to http://newbuildbot.phase1.onzo.com/onpi/pypi/
        Server response (200): OK


