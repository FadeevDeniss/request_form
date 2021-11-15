from django.db import models

class Credentials(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    email = models.EmailField()
    checkbox = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f'creator {self.name}, created at {self.created_at}'

