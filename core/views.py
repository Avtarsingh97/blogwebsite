from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse
# Create your views here.

def frontpage(request):
    posts =Post.objects.filter(status=Post.ACTIVE)
    return render(request, 'core/frontpage.html', {'posts':posts})

def about(request):
    return render(request, 'core/about.html')

def robots_txt(request):
    text=[
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")