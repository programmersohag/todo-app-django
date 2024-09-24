from django.urls import path

from todoApp import views
from todoApp.views import TodoListCreateView, TodoDetailView, AllTodosListView, TodoDeleteView, TodoUpdateView

urlpatterns = [
    path('', views.create_todo_view, name='todo_url'),
    path('show/', views.show_todo_view, name='show_url'),
    path('up/<int:f_id>', views.update_todo_view, name='update_url'),
    path('del/<int:f_id>', views.delete_todo_view, name='delete_url'),
    path('todos/', TodoListCreateView.as_view()),
    path('todos/<int:pk>/', TodoDetailView.as_view()),
    path('todos/all/', AllTodosListView.as_view()),
    path('todos/delete/<int:pk>/', TodoDeleteView.as_view()),
    path('todos/update/<int:pk>/', TodoUpdateView.as_view()),
]
