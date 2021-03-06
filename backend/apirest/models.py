from django.db import models

class Printer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    description = models.TextField()

    class Meta:
        ordering = ['name']