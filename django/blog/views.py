from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Blog
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.

class BlogListViews(ListView):
    model = Blog
    template_name = "blog/blog_list.html"



# 1
# def Detailviews(request,BlogId):
#     vlog = Blog.objects.get(id=BlogId)
#     context= {"Blog":vlog}
#     return render(request,"blog/detail.html",context)


# 2
class BlogDetailviewa(DetailView):
    model = Blog
    template_name = 'blog/detail.html'




class BlogPostViews(CreateView):
    model = Blog
    template_name = "blog/new.html"
    fields =['title','body','author']


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = "blog/edit.html"
    fields = ['title','body']


class BlogDeletePost(DeleteView):
    model = Blog
    template_name ="blog/delete.html" 
    success_url= reverse_lazy("blog:blog_list")