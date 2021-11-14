from django.db import models

class Credentials(models.Model):
    name = models.CharField(label='Your name', max_length=50)
    description = models.TextField(label='Problem description', max_length=250)
    email = models.EmailField()
    checkbox = models.BooleanField(name='Personal data processing agreement')
    created_at = models.DateTimeField(auto_now_add=True)

