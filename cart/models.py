from django.db import models
from mysite.models import user
from product.models import Product

# Create your models here.
class Cart(models.Model):
    users=models.ForeignKey(user,on_delete=models.CASCADE,related_name='carts')
    products=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='carts')
    quantity=models.IntegerField()

    def __str__(self):
        return 'Cart'