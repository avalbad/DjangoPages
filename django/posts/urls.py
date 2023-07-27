from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('',views.PostListViews.as_view(),name='post_list'),
]

