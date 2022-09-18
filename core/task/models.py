from django.db import models

from django.template.defaultfilters import slugify

from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=4000, null=True, blank=True)
    slug = models.SlugField(max_length=150, null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updatet_by = models.ForeignKey(User, related_name='+', null=True, on_delete=models.CASCADE)
    updatet_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Task, self).save(*args, **kwargs) 

    def __str__(self):
        return self.name
    
 