from django.db import models
from Explorer.models import Language, WorkLanguage

class Chapter(models.Model):
    work_language = models.ForeignKey(WorkLanguage)
    title = models.CharField(max_length=200)
    text = models.TextField()
    def __unicode__(self):
        return self.title