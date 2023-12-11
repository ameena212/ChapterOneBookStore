from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=200)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/imagesSite/")
    contact = models.CharField(max_length=100, default='N/A')
    country = models.CharField(max_length=50, default='Unknown')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default="not provided")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-details', args=[str(self.id)])
