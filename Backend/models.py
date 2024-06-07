from django.db import models

# Create your models here.
class category_db(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Description = models.CharField(max_length=500,null=True,blank=True)
    Photo = models.ImageField(upload_to="category_images",null=True,blank=True)

class product_db(models.Model):
    Product_Name = models.CharField(max_length=100,null=True,blank=True)
    Category = models.CharField(max_length=100,null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Product_Description = models.CharField(max_length=500,null=True,blank=True)
    Product_Photo = models.ImageField(upload_to="product_images",null=True,blank=True)





