from django.shortcuts import render, get_object_or_404
from .models import Category, Post

def post_list(request, category_slug=None):
    posts = Post.objects.all()
    categories = Category.objects.all()

    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)

    context = {
        "title": "Головна сторінка",
        "posts": posts,
        "categories": categories,
        "category": category
    }

    return render(request, "main/posts_list.html", context)

def post_detail(request, id, slug):
    post = get_object_or_404(Post, id=id, slug=slug)
    post.views += 1
    post.save()

    context = {
        "title": post.title,
        "post": post
    }

    return render(request, "main/post_detail.html", context)