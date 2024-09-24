from django.shortcuts import redirect, render
from rest_framework import generics
from rest_framework.response import Response

from todoApp.TodoSerializer import TodoSerializer
from todoApp.forms import TodoForm
from todoApp.models import Todo


def create_todo_view(request):
    form = TodoForm
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    template_name = "todoApp/todo.html"
    context = {"form": form}
    return render(request, template_name, context)


def show_todo_view(request):
    obj = Todo.objects.all()
    template_name = "todoApp/show.html"
    context = {"obj": obj}
    return render(request, template_name, context)


def update_todo_view(request, f_id):
    obj = Todo.objects.get(id=f_id)
    form = TodoForm(instance=obj)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    template_name = "todoApp/todo.html"
    context = {"form": form}
    return render(request, template_name, context)


def delete_todo_view(request, f_id):
    obj = Todo.objects.get(id=f_id)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    template_name = "todoApp/confirmation.html"
    context = {"obj": obj}
    return render(request, template_name, context)


class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class AllTodosListView(generics.ListAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class TodoUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    partial = True


class TodoDeleteView(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("delete Movie"))
