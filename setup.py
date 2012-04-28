from setuptools import setup, find_packages

VERSION = open('apptemplate/version.txt').read()

setup(
    name='apptemplate',
    version=VERSION,
    description='XXXXXXXXX',
    long_description=open('README.rst').read(),
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