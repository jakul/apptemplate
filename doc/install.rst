Installation
============

After downloading *apptemplate* the following changes need to be made before
you start writing your project:

* Rename the main *apptemplate* directory to the name of your application.
* In the newly named directory, similarly rename the inner *apptemplate* directory.
* Open CHANGLELOG.rst and delete everything beneath the ChangeLog heading.
* Open Makefile and change the APPNAME from *apptemplate* to the name of your application.
* Open README.rst and replace *apptemplate* with the name of your application.
* Open setup.py 
    * replace *apptemplate* with the name of your application.
    * Comment out the *url* and *download_url* parameters in the setup command.
* Open settings.py and replace all instances of *apptemplate* with your application name.
* Open doc/conf.py and replace *apptemplate* with the name of your application.
* Open app_name/views.py and replace *apptemplate* with the name of your application.
* Open app_name/tests/__init__.py and replace *apptemplate* with the name of your application.
* Open app_name/tests/views.py and replace *apptemplate* with the name of your application.


At this point you should be able to install the application (where app_dir is the directory
containing setup.py)::

    $ pip install -e /path/to/app_dir
    

Dependencies
------------

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
The standard sytax for running PyUnit tests can be used::

    # Ensure the environment the application has been installed into has been activated.
    
    $ python runtests.py
    
    $ python runtests.py apptemplate
    
    $ python runtests.py apptemplate.TestCase
    
    $ python runtests.py apptemplate.TestCase.test_method
    



