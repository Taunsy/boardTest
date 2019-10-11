from django.urls import path
from . import views

urlpatterns = [
    path('lists/', views.lists),
    path('write/', views.write),
    path('read/<int:num>/', views.read),
    path('create/', views.create)
]
