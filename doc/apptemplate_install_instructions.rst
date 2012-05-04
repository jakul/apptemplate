.. include:: global.rst

Using *apptemplate* as a base for your app
==========================================
After downloading *apptemplate* the following changes need to be made before
you start writing your project:

* Rename the main *apptemplate* directory to the name of your application.
* In the newly named directory, similarly rename the inner *apptemplate* directory.
* Open CHANGLELOG.rst and delete everything beneath the ChangeLog heading.
* Open Makefile and change the APPNAME from *apptemplate* to the name of your application.
* Open *global.rst* and update the global variables.
* Open setup.py 

 * Update/remove  the *url* and *download_url* parameters in the setup command.

* Open settings.py and replace all instances of *apptemplate* with your application name.
* Open doc/conf.py and replace *apptemplate* with the name of your application.
* Open app_name/tests/__init__.py and replace *apptemplate* with the name of your application.
* Remove doc/apptemplate_install_instructions.rst
