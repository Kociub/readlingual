from django.shortcuts import render_to_response, HttpResponseRedirect
from web_search import google

def search(request):
        query = request.REQUEST.get("query", "")
        if query not in [None, '']:
            return HttpResponseRedirect("https://www.google.com/search?q="+query+"+site:readlingual.com");
        return render_to_response('search.html') 
        