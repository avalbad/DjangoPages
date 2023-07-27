from django.urls import path
from .import views



app_name = "blog"
urlpatterns =[
    path('',views.BlogListViews.as_view(),name= "blog_list"),
    path('<int:pk>/',views.BlogDetailviewa.as_view(),name = "blogid"),
    path('new/',views.BlogPostViews.as_view(),name="new"),
    path('<int:pk>/edit/',views.BlogUpdateView.as_view(),name= "edit"),
    path('<int:pk>/delete/',views.BlogDeletePost.as_view(),name= "delete"),
]
