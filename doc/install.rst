Installation
============

After downloading *apptemplate* the following changes need to be made before
you start writing your project:

* Rename the main *apptemplate* directory to the name of your application.
* In the newly named directory, similarly rename the inner *apptemplate* directory.
* Open CHANGLELOG.rst and delete everything beneath the ChangeLog heading.
* Open Makefile and replace *apptemplate* with the name of your application.
* Open README.rst and replace *apptemplate* with the name of your application.
* Open setup.py 
    * replace *apptemplate* with the name of your application.
    * Comment out the *url* and *download_url* parameters in the setup command.
* Open doc/conf.py and replace *apptemplate* with the name of your application.
* Open *doc/sampleproj/sampleproj/settings.py* and replace *apptemplate* in the
  *INSTALLED_APPS* with the name of your application.
* Open *doc/sampleproj/sampleproj/urls.py* and replace *apptemplate* in the 
  urlpatterns with the name of your application.


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
*dependency_links* must include the project name and version number::

    dependency_links = [
        'http://github.com/jakul/python-semver/tarball#egg=semver-0.0.1',
        ...
    ]

If downloading from github you may also want to specifiy the desired commit number::

    dependency_links = [
        'http://github.com/jakul/python-semver/tarball/857113414bce76754f80422bd77f8585e75e873c#egg=semver-0.0.1',
        ...
    ]



