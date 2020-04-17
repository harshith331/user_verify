from django.db import models

# Create your models here.
class user(models.Model):
    first_name=models.CharField(max_length=128,blank=True,null=True,default="")
    last_name=models.CharField(max_length=128,blank=True,null=True,default="")
    date_of_birth=models.CharField(max_length=128,blank=True,null=True,default="")
    country_of_residence=models.CharField(max_length=128,blank=True,null=True,default="")
    state=models.CharField(max_length=128,blank=True,null=True,default="")
    city_of_residence=models.CharField(max_length=128,blank=True,null=True,default="")
    phone_no=models.CharField(max_length=15,default="")
    fav_gnr_writing=models.CharField(max_length=128,blank=True,null=True,default="")
    email=models.CharField(max_length=128,blank=True,null=True,default="")
    password=models.CharField(max_length=30,default="",blank=True,null=True)
    ready=models.BooleanField(default=False)
    doc_url=models.CharField(max_length=30,default="",blank=True,null=True)
    otp=models.CharField(max_length=30,default="",blank=True,null=True)
    short_story=models.TextField(default="")
