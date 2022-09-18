from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.db.models import Q #Required

from .forms import CategoryForm, TaskForm
from .models import Category, Task
from datetime import datetime
from time import mktime, time, localtime
# Create your views here.

class getCategory(ListView):
    model = Category
    template_name = 'task/index.html'

    

class createCategory(CreateView):
    model = Category
    form_class = CategoryForm 
    template_name= 'task/create.html'
    success_url = '/'


class getTask(ListView):
    model = Task
    template_name = 'task/index.html'
    context_object_name = 'tasks'
    queryset = Task.objects.all()
    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            object_list = self.model.objects.filter(Q(name__icontains = q) | Q(description__icontains = q)  )
        else:
            object_list = self.model.objects.all()
        return object_list
    
class getById(ListView):
    model = Task
    template_name = 'task/index.html'
    context_object_name = 'tasks'

    def get_queryset(self, *args, **kwargs):
        return Task.objects.filter(id=self.kwargs.get('id'))

class createTask(CreateView):
    model = Task
    form_class = TaskForm 
    template_name= 'task/create.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(createTask, self).form_valid(form)
        

class UpdateTask(UpdateView):
    model = Task
    form_class = TaskForm 
    template_name= 'task/update.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.updatet_by = self.request.user
        form.instance.slug = self.request.title
        return super(UpdateTask, self).form_valid(form)


class DeleteView(DeleteView):
    model = Task
    template_name = 'task/index.html'
    success_url = '/'

    
    