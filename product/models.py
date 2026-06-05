from django.db import models
from category.models import Category
# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    offers=models.CharField(max_length=100)
    quantity=models.IntegerField()
    description=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.product_name