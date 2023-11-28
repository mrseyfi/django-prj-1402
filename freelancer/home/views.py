from datetime import datetime
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact
from django.contrib import messages


def main_page(request):
    return render(request, template_name='home/main.html')


def contact_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Contact.objects.create(fullname=cd['fullname'],
                                   email=cd['email'],
                                   phone=cd['phone'],
                                   message=cd['message'],
                                   created=datetime.now())
            messages.success(request, 'Thank you! Your message has been successfully sent.')
            return redirect('home')

    else:
        form = ContactForm()

    # person = {'name': 'admin'}
    # return render(request, template_name='home/contact.html', context=person)
    return render(request, template_name='home/contact.html', context={'form': form})


def about_page(request):
    return render(request, template_name='home/about.html')


def portfolio_page(request):
    return render(request, template_name='home/portfolio.html')


