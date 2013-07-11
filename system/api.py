from tastypie.resources import ModelResource
from tastypie import fields

from system.models import Language

from dbs.models import Journey


class LanguageResource(ModelResource):

    class Meta:
        queryset = Language.objects.all()
        resource_name = 'language'
        allowed_methods = ['get']


class JourneyResource(ModelResource):
    language = fields.ForeignKey(LanguageResource, 'language')

    class Meta:
        queryset = Journey.objects.all()
        resource_name = 'journey'
        allowed_methods = ['get']
        filtering = {
            'language': ('exact',),
        }
