from django.db import models

# Create your models here.

from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)
    url = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Menu'
