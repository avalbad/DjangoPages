from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path( 'posts/',include('posts.urls')),
    path( 'blog/',include('blog.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/',include('accounts.urls')),
    path( '',include('pages.urls')),
]
