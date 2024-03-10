from django.urls import path
from . import views

urlpatterns = [
  path('test/', views.test),
  path('todos/', views.todos),
  path('add_todo/', views.add_todo),
  path('delete_todo/', views.delete_todo),
  path('set_complete/', views.setComplete),
  path('set_not_complete/', views.setNotComplete)
]