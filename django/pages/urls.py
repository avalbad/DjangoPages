from django.urls import path
from . import views

app_name = "asd" 
urlpatterns = [
path('',views.HomepageViews.as_view(),name="home"),
path('about/',views.AboutViews.as_view(),name ="about"),
]
