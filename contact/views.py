
# Create your views here.
from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse

def index(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        textarea=request.POST.get('textarea')
        contact.name=name
        contact.email=email
        contact.textarea=textarea
        contact.save()
        return HttpResponse("<h1>Thanks for contact us!</h1>")

    return render(request, 'contact.html')