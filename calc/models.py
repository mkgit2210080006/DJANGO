from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=200,null=True)
    age=models.IntegerField(max_length=100,null=True)
    email=models.CharField(max_length=300,null=True)
    dateCreated=models.DateTimeField(auto_now_add=True,null=True)

    def _str_(self):
        return self.name
    
class Tag(models.Model):
        name=models.CharField(max_length=200,null=True)
    
        def _str_(self):
            return self.name
    
    
class Product(models.Model):
        CATEGORY=(
            ('Indoor','Indoor'),
            ('Outdoor','Outdoor')
        )

        name=models.CharField(max_length=200,null=True)
        price=models.FloatField(max_length=200,null=True)
        category=models.CharField(max_length=200,null=True,choices=CATEGORY)
        tags=models.ManyToManyField(Tag)

        def _str_(self):
            return self.name
class Order(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('Out of Delivery','Out of Delivery'),
        ('Delivered','Delivered')
    )
    Customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    Product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    status=models.CharField(max_length=200,null=True,choices=STATUS)