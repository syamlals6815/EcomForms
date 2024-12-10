from django.db import models



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    product_image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock  = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

