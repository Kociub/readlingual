from django.db import models

class Language(models.Model):
    title = models.CharField(max_length=200)
    short_title = models.CharField(max_length=2)
    def __unicode__(self):
        return self.title

class Work(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    original_language = models.ForeignKey(Language)
    def __unicode__(self):
        return self.title

class WorkLanguage(models.Model):
    work = models.ForeignKey(Work)
    language = models.ForeignKey(Language)
    title = models.CharField(max_length=200)
    summary = models.TextField()
    def __unicode__(self):
        return self.title +"\\"+ self.language.short_title

