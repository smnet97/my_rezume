from django.db import models


class ContactModel(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
        ordering = ('-id',)
