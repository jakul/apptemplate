"""
Example docs about apptemplate module
"""
import semver as _semver
import os
_version_path = os.path.join(os.path.dirname(__file__), 'version.txt')

VERSION = open(_version_path).read().rstrip() #rstrip() removes newlines
VERSION_INFO = _semver.parse(VERSION)
AUTHOR = 'some author'
AUTHOR_EMAIL = 'someemail@invalid.com'
PROJECT_NAME = os.path.split(os.path.dirname(os.path.abspath(__file__)))[-1]
SHORT_DESCRIPTION = 'some info about this project'