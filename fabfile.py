import os
import datetime
from fabric.utils import abort, puts
import semver
import apptemplate
from fabric.operations import local
try:
    import readline # This module gives line editing and history
except ImportError:
    pass

_CHANGELOG_MESSAGE = '.changelog_message'
_CHANGELOG = 'CHANGELOG.rst'
_CHANGELOG_TEMPLATE = 'doc/.changelog_message_template'
_VERSION_FILE = 'apptemplate/version.txt'
_EDITOR_COMMAND = 'vi %(file)s +3'
_DATE_FORMAT = '%d/%m/%Y'
_ONPI_UPLOAD_COMMAND = 'python setup.py sdist upload -r onpi'

def release(version=None):
    if version is None:
        version = get_version_number()
    
    puts('Releasing version %(version)s' % {'version': version}) 
      
    # Get changelog message
    reset_changelog_message(version)
    message = get_changelog_message()
    
    # Add it to changelog
    update_changelog(message)
    
    # Update version.txt
    update_version_file(version)
    
    # Upload to PyPI server
    upload_to_onpi()
    
    
    puts('Version %(version)s released successfully' % {'version': version}) 
    
def get_version_number():
    """
    Prompts the user to enter the version number being released. 
    Outputs the current version number.
    """
    context = {}
    context['current_version'] = apptemplate.VERSION
  
    puts('Current version: %(current_version)s' % context)
    new_version = None
    input = None
    while not new_version:
        if input is not None:
            puts('Invalid version number')
            
        input = raw_input('Enter the new version number: ')
        print input
        try:
            semver.parse(input)
        except ValueError:
            pass
        else:
            new_version = input
            
    return new_version
     
def reset_changelog_message(version):  
    """
    Reset the changelog message file so that the user can enter a new message.
    """      
    with open(_CHANGELOG_TEMPLATE, 'r') as template:
        template_content = template.read()
        
    with open(_CHANGELOG_MESSAGE, 'w') as message:
        message.write(template_content % {'date': datetime.date.today().strftime(_DATE_FORMAT), 'version': version})
    
def get_changelog_message():
    """
    Prompt the user to write the changelog message.
    The date and version number are automatically written out, but the user
    can change them if they want.
    The lines with instructions (prefixed with 'ONZO:') are stripped out of the
    content
    """ 
    os.system(_EDITOR_COMMAND % {'file': _CHANGELOG_MESSAGE})
    
    with open(_CHANGELOG_MESSAGE) as message:
        message_content = [
            line for line in message if not line.startswith('ONZO:') and \
            line not in ['\n', '\r\n']
        ]
    
    return message_content
    
def update_changelog(message): 
    """
    Updates the changelog with the given message.
    The message is inserted at the top of the file, after the file title
    """ 
    output = []
    with open(_CHANGELOG, 'r') as changelog:
        content = changelog.readlines()
        
    # Output the file header
    output.extend(content[0:3])
    
    # Output the new content
    output.extend(message)
    
    # Ensure there is a space between the changelog messages
    output.append('\n')
    
    #output the existing content
    output.extend(content[3:])
    
    with open(_CHANGELOG, 'w') as changelog:
        changelog.write(''.join(output))
    
def update_version_file(version):
    with open(_VERSION_FILE, 'w') as version_file:
        version_file.write(version)
        
def upload_to_onpi():
    local(_ONPI_UPLOAD_COMMAND)