from django.shortcuts import render_to_response
from web_search import google

def search(request):
        params = {}
        query = request.REQUEST.get("query", "")
        if query not in [None, '']:
            params['query'] = query
            search_blocking = google(query, 10)
            params['result'] = search_blocking
            for (name, url, desc) in search_blocking:
                print name, url
        return render_to_response('search.html', params) 
        