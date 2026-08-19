from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Category Name')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Category Slug')
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('main:post_list_by_category', args=[self.slug])

    def __str__(self):
        return f"{self.name}"
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='post_images', blank=True)
    views = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('main:post_detail', args=[self.slug])
    
    def __str__(self):
        return f"{self.title} - {self.created_at}"

