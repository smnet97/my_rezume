from django.db import models
from ckeditor.fields import RichTextField

class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    category = models.ManyToManyField(CategoryModel, related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
        ordering = ('-id',)