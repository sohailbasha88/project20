from django.db import models

# Create your models here.

class country(models.Model):
    cid=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=100)
    cpl=models.IntegerField()
class state(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=100)
    spl=models.IntegerField()
    cid=models.ForeignKey(country,on_delete=models.CASCADE)