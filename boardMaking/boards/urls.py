from django.urls import path
from . import views

urlpatterns = [
    path('lists/', views.lists),
    path('write/', views.write),
    path('read/<int:boardId>/', views.read),
    path('create/', views.create),
    path('displayUpdate/<int:boardId>/', views.displayUpdate),
    path('update/<int:boardId>/', views.update),
    path('delete/<int:boardId>/', views.delete),
    path('read/<int:boardId>/createComment/', views.createComment),
    path('read/<int:boardId>/deleteComment/<int:commentId>/', views.deleteComment),
    path('read/<int:boardId>/comment/<int:commentId>/createReComment/',
         views.createReComment),
    path('read/<int:boardId>/comment/<int:commentId>/deleteReComment/<int:reCommentId>/',
         views.deleteReComment)
]
