from django.shortcuts import render

# Create your views here.

def main_page(request):
    return render(request, template_name='index.html')

def contact_page(request):
    person = {'name': 'admin'}
    return render(request, template_name='home/contact.html', context=person)

def about_page(request):
    person = {'name': 'admin'}
    return render(request, template_name='home/about.html', context=person)