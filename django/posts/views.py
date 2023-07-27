from django.shortcuts import render
from .models import post
from django.views.generic import ListView
# Create your views here.

# 1
# def post_list(request):
#     posts = post.objects.all()
#     return render(request,"post/list.html",{"posts":posts})



# 2
class PostListViews(ListView):
    model = post
    template_name = "posts/list.html"
    context_object_name = "posts"

