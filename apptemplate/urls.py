from django.conf.urls.defaults import *
from views import *

urlpatterns = patterns('',
    url('^$', hello),   
    url('^version/$', version, name='version'),   
)
