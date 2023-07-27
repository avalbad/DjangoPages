from typing import List, Optional, Set
from django.db import models
from django.urls import reverse
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    author = models.ForeignKey("auth.user",on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse("blog:blogid",args=[str(self.id)])
        # return reverse("blog:blogid",kwargs={"pk":self.id})
        
    



