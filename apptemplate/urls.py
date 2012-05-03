from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    url('^version/$', version, name='version'),   
)
