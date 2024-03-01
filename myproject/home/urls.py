from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('/about', views.about, name="about"),
    path('/recent', views.recent, name="recent"),
    path('blog/<id>',views.continu,name='continue_reading'),
    path('add',views.add,name='add'),
    path('insert',views.insert),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.edit, name='edit'),
    path('edit/<int:id>/', views.update, name='update'),

   
]


