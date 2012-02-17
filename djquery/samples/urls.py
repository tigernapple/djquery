from django.conf.urls.defaults import *  
from models import *  
from views import *  
  
urlpatterns = patterns('',  
    (r'hello/$', 'django.views.generic.simple.direct_to_template', {'template':'samples/hello.html'}),
)