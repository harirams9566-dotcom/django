from django.db import models

# Create your models here.
class Category(models.Model):
    category_id=models.IntegerField()
    category_name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.category_name
