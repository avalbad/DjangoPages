from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# def home(request):
#    return render(request,'pages/home.html',{})

class HomepageViews(TemplateView):
    template_name = 'pages/home.html'

class AboutViews(TemplateView):
    template_name = 'pages/about.html'

