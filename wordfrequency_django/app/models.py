from django.db import models

# Create your models here.


class SherlockBook(models.Model):
    text = models.TextField()

    def __str__(self):
        return "Sherlock Holmes"
