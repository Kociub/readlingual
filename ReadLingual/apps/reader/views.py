from django.shortcuts import render
from django.http import Http404

from readlingual.apps.reader.models import Chapter

def chapter(request, chapteroriginal_id, chapter_id):
    try:
        chapter = Chapter.objects.get(pk=chapter_id)
        chapteroriginal = Chapter.objects.get(pk=chapteroriginal_id)
        chapter_paragraphs = zip(filter(None, chapteroriginal.text.splitlines()), filter(None, chapter.text.splitlines()))
    except Chapter.DoesNotExist:
        raise Http404
    return render(request, 'reader/chapter.html', {'chapter_paragraphs': chapter_paragraphs, 'chapteroriginal': chapteroriginal, 'chapter': chapter})
