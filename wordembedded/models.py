from django.db import models

# Create your models here.

class wordembedded(models.Model):
    text=models.TextField()
    body=models.TextField()

    def __str__(self):
        return self.text[:40]

