from django.db import models

# Create your models here.
class Campaign(models.Model):
    """ The model store the information of Campaign """
    idx = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    announcer = models.CharField(max_length=20, blank=True)
    register_num = models.IntegerField(null=True)
    

class Register(models.Model):
    """ The model for store the the registing action """
    idx = models.AutoField(auto_created=True, primary_key=True)
    user = models.CharField(max_length=20)
    campaign = models.IntegerField(null=True)
    