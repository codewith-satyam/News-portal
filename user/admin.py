from django.contrib import admin
from .models import *
# Register your models here.
class tblcontactAdmin(admin.ModelAdmin):
    list_display=("name","email","mobile","message")

admin.site.register(tblcontact,tblcontactAdmin)


class tblgalleryAdmin(admin.ModelAdmin):
    list_display=("title","picture")
admin.site.register(tblgallery,tblgalleryAdmin)

class tblteamAdmin(admin.ModelAdmin):
    list_display=("name","picture","post","experience")
admin.site.register(tblteam,tblteamAdmin)

class tblcityAdmin(admin.ModelAdmin):
    list_display=("id","cityname","picture")
admin.site.register(tblcity,tblcityAdmin)  

class tblnewsAdmin(admin.ModelAdmin):
    list_display=("id","headlines","description","picture",
                  "city","category","posteddate")
admin.site.register(tblnews,tblnewsAdmin)

class tblcategoryAdmin(admin.ModelAdmin):
    list_display=("id","cname","picture")
admin.site.register(tblcategory,tblcategoryAdmin)




class tblsliderAdmin(admin.ModelAdmin):
    list_display=("id","headlines","news_info","picture","posted_date")
admin.site.register(tblslider,tblsliderAdmin)    



class tbljobsAdmin(admin.ModelAdmin):
    list_display=("id","job_title","job_link")
admin.site.register(tbljobs,tbljobsAdmin) 

class tblvdonewsAdmin(admin.ModelAdmin):
    list_display=("id","title","news_info","video_link","city",
                  "category","posted_date")
admin.site.register(tblvdonews,tblvdonewsAdmin) 





