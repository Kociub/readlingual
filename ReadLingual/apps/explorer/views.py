from django.shortcuts import render
from django.http import Http404

from readlingual.apps.explorer.models import Work, WorkLanguage
from readlingual.apps.reader.models import Chapter

def index(request):
    latest_work_list = Work.objects.all().order_by('-publication_date')[:5]
    context = {'latest_work_list': latest_work_list}
    return render(request, 'explorer/works.html', context)

def work(request, work_id):
    try:
        work = Work.objects.get(pk=work_id)
    except Work.DoesNotExist:
        raise Http404
    return render(request, 'explorer/work.html', {'work': work})

def worklanguage(request, work_id, worklanguage_id):
    try:
        worklanguage = WorkLanguage.objects.get(pk=worklanguage_id)
        work = Work.objects.get(pk=work_id)
        worklanguageoriginal = WorkLanguage.objects.get(language=work.original_language)
        worklanguageoriginal_chapters = Chapter.objects.filter(work_language=worklanguageoriginal.language)
        worklanguage_chapters = Chapter.objects.filter(work_language=worklanguage)
        chapters = zip(worklanguageoriginal_chapters, worklanguage_chapters)
    except Work.DoesNotExist:
        raise Http404
    return render(request, 'explorer/worklanguage.html', {'worklanguage_title': worklanguage.title, 'worklanguageoriginal_title': worklanguageoriginal.title, 'chapters': chapters,})