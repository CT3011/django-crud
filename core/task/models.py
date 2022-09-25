from symbol import import_as_name
from django.db import models
from django.db.models import TextChoices 
from django.utils.translation import gettext_lazy as _

from django.template.defaultfilters import slugify

from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Task(models.Model):

    class Options(TextChoices):
        SPECIFIC = 'spacific', _('spacific')
        ALL = 'all', _('all')
        DEP = 'dep', _('dep')

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.CharField(max_length=10, choices=Options.choices, default='all')
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
    
 