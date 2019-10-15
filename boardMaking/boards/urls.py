from django.urls import path
from . import views

urlpatterns = [
    path('lists/', views.lists),
    path('write/', views.write),
    path('read/<int:num>/', views.read),
    path('create/', views.create),
    path('displayUpdate/<int:num>/', views.displayUpdate),
    path('update/<int:num>/', views.update),
    path('delete/<int:num>/', views.delete)
]
