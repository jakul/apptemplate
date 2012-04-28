import semver as _semver
import os
_version_path = os.path.join(os.path.dirname(__file__), 'version.txt')
VERSION = open(_version_path).read().rstrip() #rstrip() removes newlines
VERSION_INFO = _semver.parse(VERSION)