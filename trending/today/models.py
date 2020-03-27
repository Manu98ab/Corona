from django.db import models

# Create your models here.
class manunews(models.Model):
    newsid = models.AutoField(primary_key=True)
    headline = models.CharField(max_length=1000,default='')
    content = models.CharField(max_length=2000,default='')
    image = models.TextField(max_length=10000, default='')
    link = models.CharField(max_length=500, default='')
    channel = models.CharField(max_length=15,default='')
    time = models.CharField(max_length=10,default='')
    type=models.CharField(max_length=50,default='')
    def __int__(self):
        return self.newsid

class counter(models.Model):
    counterid=models.AutoField(primary_key=True)
    Total_cases=models.CharField(max_length=100,default='Unavailable')
    Deaths=models.CharField(max_length=100,default='Unavailable')
    Recovered=models.CharField(max_length=100,default='Unavailable')
