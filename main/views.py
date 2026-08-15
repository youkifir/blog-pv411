from django.shortcuts import render
from .models import Post

def post_list(request):

    posts = Post.objects.all()

    context = {
        "title": "Головна сторінка",
        "posts": posts
    }

    return render(request, "main/posts_list.html", context)
