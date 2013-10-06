from django.contrib import admin
from Explorer.models import Language, Work, WorkLanguage
from Reader.models import Chapter

class ChapterInline(admin.TabularInline):
    model = Chapter

class WorkLanguageInline(admin.StackedInline):
    model = WorkLanguage
    extra = 1
    inlines = [ChapterInline]

class WorkAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title', 'author', 'original_language']}),
        ('Date information', {'fields': ['publication_date'], 'classes': ['collapse']}),
    ]
    inlines = [WorkLanguageInline]

admin.site.register(Work, WorkAdmin)

admin.site.register(Language)

admin.site.register(Chapter)