from django.http import HttpResponse
from django.shortcuts import render

from django.db import models

blogs = ["foo", "fii", "bar"]
blog_desc = ["foo description", "fii description", "bar description"]

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()

def index(request):
    return render(request, "blog/index.html", {
        "blogs": blogs,
        "description": blog_desc
    })

def add(request):
    return render(request, "blog/add.html")