from django.urls import path
from . import views

urlpatterns=[
    path("",views.index),
    path("index/",views.index),
    path("about/",views.about),
    path("team/",views.team),
    path("gallery/",views.gallery),
    path("category/",views.category),
    path("services/",views.services),
    path("details/",views.details),
    path("contact/",views.contact),
    path("jobs/",views.jobs),
    path("vnews/",views.videonews),
    path("me/",views.me),

]