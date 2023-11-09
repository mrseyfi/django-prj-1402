from django.db import models

# python manage.py makemigrations
# python manage.py migrate


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField()