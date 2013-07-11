from django.conf.urls.defaults import *
from system.api import LanguageResource

language_resource = LanguageResource()

urlpatterns = patterns('',
    (r'^api/', include(language_resource.urls)),
)
