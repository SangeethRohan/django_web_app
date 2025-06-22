from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.TextField(max_length=200)
    description = models.TextField()   
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    summary = models.TextField(default="Default Description")

    def get_absolute_url(self):
        return reverse("products:Product-detail",kwargs={"id": self.id})
        # return f"/products/{self.id}"