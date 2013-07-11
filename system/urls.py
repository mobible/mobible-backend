from django.conf.urls.defaults import *
from system.api import LanguageResource
from tastypie.api import Api


v1_api = Api(api_name='v1')
v1_api.register(LanguageResource())

urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
)
