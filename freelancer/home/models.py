from django.db import models

# python manage.py makemigrations
# python manage.py migrate


class Contact(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    created = models.DateTimeField()

