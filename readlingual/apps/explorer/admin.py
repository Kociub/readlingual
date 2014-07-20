from django.contrib import admin
from readlingual.apps.explorer.models import Language, Work, WorkLanguage
from readlingual.apps.reader.models import Chapter

class ChapterInline(admin.TabularInline):
    model = Chapter

class WorkLanguageInline(admin.StackedInline):
    model = WorkLanguage
    extra = 1
    inlines = [ChapterInline]

class WorkAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'author', 'original_language']}),
    ]
    inlines = [WorkLanguageInline]

admin.site.register(Work, WorkAdmin)

admin.site.register(Language)

admin.site.register(Chapter)