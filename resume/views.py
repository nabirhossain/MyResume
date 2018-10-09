from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.

def index(request):
    return render(request, 'about.html')

def experience(request):
    return render(request, 'experience.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def skills(request):
    return render(request, 'skills.html')

def awards(request):
    return render(request, 'awards.html')

#def contact(request):
#    return render(request, 'contact.html')

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            your_email = form.cleaned_data['your_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, your_email, ['nabirhossain13@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'success.html')
    return render(request, 'contact.html', {'form': form})
