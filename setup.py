from setuptools import setup, find_packages
import os


def fread(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

PROJECT_NAME = os.path.split(os.path.dirname(os.path.abspath(__file__)))[-1]
VERSION = open('apptemplate/version.txt').read()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    description='XXXXXXXXX',
    long_description=fread("README.rst")+"\n\n"+fread('CHANGELOG.rst'),
    author='Craig Blaszczyk',
    author_email='masterjakul@gmail.com',
    url='https://github.com/jakul/apptemplate',
    download_url='https://github.com/jakul/apptemplate/downloads',
    packages=find_packages(),
    install_requires=open('requirements.txt').read(),
    dependency_links = [
        # This is for requirements not on PyPi
        'http://github.com/jakul/python-semver/tarball/master#egg=python-semver'
    ],
    include_package_data=True,
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