from django.shortcuts import render_to_response, HttpResponseRedirect
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def search(request):
    query = request.REQUEST.get("query", "")
    if query not in [None, '']:
        return HttpResponseRedirect("https://www.google.com/search?q="+query+"+site:readlingual.com");
    return render_to_response('search.html')

def contact(request):
    name = request.REQUEST.get("name", "")
    email = request.REQUEST.get("email", "")
    subject = request.REQUEST.get("subject", "")
    message = request.REQUEST.get("message", "")
    
    if name and email and subject and message:
        try:
            validate_email( email )
        except ValidationError:
            return render_to_response('contact.html', {'name':name,'email':email,'subject':subject,'message':message,'error_message': "Email is not correct"})
        
        send_mail(subject, name + ", " + message, email,['jakub.kociubinski@gmail.com'], fail_silently=False)
        
        return render_to_response('contact_success.html')
    else:
        if 'name' in request.GET:
            return render_to_response('contact.html', {'name':name,'email':email,'subject':subject,'message':message,'error_message': "some required fields are empty"})
        else:
            return render_to_response('contact.html')