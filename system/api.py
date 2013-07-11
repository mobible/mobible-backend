from tastypie.resources import ModelResource
from system.models import Language


class LanguageResource(ModelResource):

    class Meta:
        queryset = Language.objects.all()
        resource_name = 'language'
