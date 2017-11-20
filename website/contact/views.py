from django.shortcuts import render
# from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact
from django.http import HttpResponseRedirect

# Create your views here.
def contact(request):
    form = ContactForm()
    return render(request,"contact.html",{"form":form})

def saving_contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        contato_enviado = Contact(name=form.cleaned_data['name'],
                                  email=form.cleaned_data['email'],
                                  phone=form.cleaned_data['phone'],
                                  subject=form.cleaned_data['subject'],
                                  message=form.cleaned_data['message'])
        contato_enviado.save()
    return HttpResponseRedirect('/')
