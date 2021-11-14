from django.db import models

class Credentials(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    email = models.EmailField()
    checkbox = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

