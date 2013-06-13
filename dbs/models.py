from django.db import models


class Journey(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class Verse(models.Model):
    journey = models.ForeignKey(Journey)
    index = models.PositiveIntegerField(
        help_text='The position of this verse in relation to other '
                  'verses for this Journey')
    context = models.TextField(
        help_text='The context for this verse that is sent via SMS')
    verse = models.TextField(
        help_text='The verse text sent via SMS.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s - %s' % (self.verse, self.context)
