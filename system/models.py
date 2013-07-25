from django.db import models


class Language(models.Model):
    language_code = models.CharField(max_length=6)
    display_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.display_name


class Introduction(models.Model):
    language = models.ForeignKey(Language)
    text = models.TextField()

    def __unicode__(self):
        return self.text
