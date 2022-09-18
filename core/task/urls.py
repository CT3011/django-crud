from django.urls import path

from . import views


urlpatterns = [
    # path('', views.getCategory.as_view(), name='get_category'),
    path('', views.getTask.as_view(), name='home'),
    # path('create/', views.createCategory.as_view(), name='create_category'),
    path('create/', views.createTask.as_view(), name='create_task'),
    path('update/<int:pk>/', views.UpdateTask.as_view(), name='update_task'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete_task'),
    
]
