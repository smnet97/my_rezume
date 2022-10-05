from django.db import models
from ckeditor.fields import RichTextField


class WorkCategoryModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class WorkModel(models.Model):
    title = models.CharField(max_length=100)
    body = RichTextField()
    category = models.ManyToManyField(WorkCategoryModel, related_name='works')
    image = models.ImageField(upload_to='works')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'work'
        verbose_name_plural = 'works'
