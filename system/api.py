from tastypie.resources import ModelResource
from tastypie import fields

from system.models import Language, Introduction

from dbs.models import Journey


class LanguageResource(ModelResource):

    class Meta:
        queryset = Language.objects.all()
        resource_name = 'language'
        allowed_methods = ['get']


class JourneyResource(ModelResource):
    language = fields.ForeignKey(LanguageResource, 'language', full=True)

    class Meta:
        queryset = Journey.objects.all()
        resource_name = 'journey'
        allowed_methods = ['get']
        filtering = {
            'language': ('exact',),
        }


class IntroductionResource(ModelResource):
    language = fields.ForeignKey(LanguageResource, 'language', full=True)

    class Meta:
        queryset = Introduction.objects.all()
        resource_name = 'introduction'
        allowed_methods = ['get']
        filter = {
            'language': ('exact',),
        }
