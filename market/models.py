from django.db import models

# Create your models here.
class Item(models.Model):
    idx = models.AutoField(auto_created=True, primary_key=True)
    user = models.CharField(max_length=100, default='visitor')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    transaction_type = models.CharField(max_length=20)
    transaction_location = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=20)
    condition = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')


class Love(models.Model):
    user = models.CharField(max_length=100)
    item = models.IntegerField(null=True)

class Comment(models.Model):
    item_idx = models.IntegerField(null=True)
    username = models.CharField(max_length=100, default='visitor')
    contents = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
