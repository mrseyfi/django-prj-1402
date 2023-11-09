from django.shortcuts import render
from .models import Post

def main_page(request):
    return render(request, template_name='index.html')

def contact_page(request):
    person = {'name': 'admin'}
    return render(request, template_name='home/contact.html', context=person)

def about_page(request):
    return render(request, template_name='home/about.html')

def portfolio_page(request):
    return render(request, template_name='home/portfolio.html')