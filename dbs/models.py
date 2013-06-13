from django.db import models


class Journey(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class Verse(models.Model):
    journey = models.ForeignKey(Journey)
    index = models.IntegerField()
    context = models.TextField()
    verse = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s - %s' % (self.verse, self.context)
