from django.shortcuts import render
from django.http import HttpResponse

from django.db.models import Q
from .models import *

# Create your views here.

def index(request):
    sdata=tblslider.objects.all().order_by("-id")[0:2]
    vdata=tblvdonews.objects.all().order_by("-id")[0:4]
    cdata=tblcategory.objects.all().order_by("id")[0:12]
    cities=tblcity.objects.all().order_by("-id")
    jobs=tbljobs.objects.all().order_by("-id")[0:4]
    news=tblnews.objects.all().order_by("-id")[0:12]
    d={"ct":cities,"jobs":jobs,"topnews":news ,"cat":cdata,"vnews":vdata,"slider":sdata}


    return render(request,"index.html",d)

def about(request):
    return render(request,"about.html")

def team(request):
    teamdata=tblteam.objects.all()
    d={"tea":teamdata}
    return render(request,"team.html",d)

def gallery(request):
    data=tblgallery.objects.all()
    d={"gal":data}
    return render(request,"gallery.html",d)

def category(request):
    x=request.GET.get("search")
    data=tblcity.objects.all().order_by("-id")
    cityid=request.GET.get("msg")
    id=request.GET.get('id')
    if id :
        ndata=tblnews.objects.filter(category=id).order_by("-id")
    elif cityid:
        ndata=tblnews.objects.filter(city=cityid).order_by("-id")  

    elif x:
        ndata=tblnews.objects.filter(Q(headlines__icontains=x)|Q(description__icontains=x) )

    else:    
        ndata=tblnews.objects.all().order_by("-id")
    cdata=tblcategory.objects.all()
    d={"cities":data,"news":ndata,"cat":cdata}
    return render(request,"category.html",d)

def services(request):
    return render(request,"services.html")


def details(request):
    x=request.GET.get("nid")
    data=tblnews.objects.all().filter(id=x)
    d={"news":data}
    return render(request,"details.html",d)  

def contact(request):
        
    if request.method=="POST":
        Name=request.POST.get("name")
        Mobile=request.POST.get("mob")
        Email=request.POST.get("email")
        Message=request.POST.get("msg")
        tblcontact(name=Name,email=Email,mobile=Mobile,message=Message).save()     #name,email,mobile,message=contact ka field name
        return HttpResponse("<script>alert('Data Saved Successfully');location.href='/contact/'</script>")

    return render(request,"contact.html")   



def jobs(request):
    jobs=tbljobs.objects.all().order_by("-id")
   
    d={"jobs":jobs}
    return render(request,"jobs.html",d)

def videonews(request):
    data=tblvdonews.objects.all().order_by("-id")
    d={"vnews":data}
    return render(request,"videonews.html",d)    





def me(request):
    return render(request,"me.html")    


