from django import forms

from .models import Category , Task

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['category', 'name', 'description']
        
  