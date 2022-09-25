from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.db.models import Q #Required
from django.views import View
from django.core.exceptions import ObjectDoesNotExist

from .forms import CategoryForm, TaskForm
from .models import Category, Task
from datetime import date, datetime
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

# _______________________________________
class createTask(CreateView):
    form_class = TaskForm 
    template_name = 'task/create.html'
    success_url = '/'

    print(">>>>>>>>>>>>>>>>>>>>Class instance")

    def form_valid(self, form):
        print("Data......................", form.instance.name)
        form.instance.created_by = self.request.user
        try:
            Task.objects.get(category=form.instance.category, subcategory=form.instance.subcategory)
            response = {'error': "Already exist task with same category and subcategory"}
            print(response)
            return render(self.request, 'task/index.html',response)
        except:
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


class CreateTaskValidationView(View):
    form_class = TaskForm 
    template_name = 'task/create.html'
    

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, "task/create.html", {'form': form})
    

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            
            #____________saperate______________
            # try:
            #     Task.objects.get(category=form.instance.category, subcategory=form.instance.subcategory)
            #     response = {'error': "Already exist task with same category and subcategory"}
            #     print(response)
            #     return redirect(reverse('home'))
            # except:
            #     form.save()
            #     return redirect(request, self.template_name, {'form': form})
            # except ObjectDoesNotExist:
            #     form.save()
            # return redirect(reverse('home'))

            
           #_____________other one_________________
            # data = list(Task.objects.all().values_list('category', 'subcategory'))
            # print(data, "#####>")
            form.instance.created_by = self.request.user
            # category =  form.instance.category
            # print(category, "_________ >>")
            # subcategory = form.instance.subcategory
            # print(subcategory, "----------------->>") 
            # instance = [('category', 'subcategory')]
            # print(instance, "*********---->>") 
            # if instance in date:
            try: 
                Task.objects.get(category=form.instance.category, subcategory=form.instance.subcategory)
                return render(request, self.template_name, {'form': form})
            except:
                form.save()
                return redirect(reverse('home'))
        else:
            return render(request, self.template_name, {'form': form})

#__________other second_______________
    # def form_valid(self, form):
    #     print("Data......................", form.instance.name)
    #     form.instance.created_by = self.request.user
    #     print(form.instance.category, "_____asdasd")
    #     print(form.instance.subcategory, "__________sdasd" )
    #     if form.instance.category and form.instance.subcategory in date:
    #         print(form.instance.category, "_____asdasd")
    #         print(form.instance.subcategory, "__________sdasd" )
    #         return render('task/index.html')
    #     else:
    #         return super(CreateTaskValidationView, self).form_valid(form)
            

