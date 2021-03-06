from setuptools import setup, find_packages
import os
from apptemplate import VERSION, AUTHOR, PROJECT_NAME, SHORT_DESCRIPTION, \
    AUTHOR_EMAIL


def fread(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='onzo' + PROJECT_NAME,
    version=VERSION,
    description=SHORT_DESCRIPTION,
    long_description=fread("README.rst")+"\n\n"+fread('CHANGELOG.rst'),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url='https://github.com/jakul/apptemplate',
    download_url='https://github.com/jakul/apptemplate/downloads',
    packages=find_packages(),
    install_requires=open('requirements.txt').read(),
    dependency_links = [
        # This is for requirements not on PyPi
        'http://github.com/jakul/python-semver/tarball/857113414bce76754f80422bd77f8585e75e873c#egg=semver-0.0.1',
    ],
    include_package_data=True,
    package_data={'':['version.txt']},
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
