from django.db import models
# Create your models here.
class tblcontact(models.Model):
    name=models.CharField(max_length=70,null=True)
    email=models.EmailField(max_length=100,null=True)
    mobile=models.CharField(max_length=20,null=True)
    message=models.TextField(null=True)

class tblgallery(models.Model):
    title=models.CharField(max_length=50)
    picture=models.ImageField(upload_to="static/gallery/", null=True)

class tblteam(models.Model):
    name=models.CharField(max_length=40,null=True)
    picture=models.ImageField(upload_to="static/gallery/",null=True)
    post=models.CharField(max_length=50,null=True)
    experience=models.CharField(max_length=50,null=True)    

class tblcity(models.Model):
    cityname=models.CharField(max_length=60,null=True)
    picture=models.ImageField(upload_to="static/city/",null=True,blank=True)
    def __str__(self):
        return self.cityname

class tblcategory(models.Model):
    picture=models.ImageField(upload_to="static/category/",null=True,blank=True)  
    cname=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.cname  

class tblnews(models.Model):
    headlines=models.TextField(null=True)
    description=models.TextField(null=True)
    picture=models.ImageField(upload_to="static/news/",null=True,blank=True)
    category=models.ForeignKey(tblcategory,on_delete=models.CASCADE,null=True)
    city=models.ForeignKey(tblcity,on_delete=models.CASCADE,null=True)
    posteddate=models.CharField(max_length=100,null=True)


class tblslider(models.Model):
     headlines=models.CharField(max_length=200,null=True)
     news_info=models.TextField(null=True)
     picture=models.ImageField(upload_to="static/slider/",null=True)
     posted_date=models.DateField(null=True)

class tbljobs(models.Model):
    job_title=models.CharField(max_length=200,null=True)
    job_link=models.CharField(max_length=200,null=True)

class tblvdonews(models.Model):
    title=models.CharField(max_length=400,null=True)
    news_info=models.TextField(null=True)
    video_link=models.CharField(max_length=200,null=True)
    city=models.ForeignKey(tblcity,on_delete=models.CASCADE,null=True)
    category=models.ForeignKey(tblcategory,on_delete=models.CASCADE,null=True)
    posted_date=models.DateField(null=True)         


