from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

def home_page(request):
    todos = Todo.objects.all()
    return render(request, 'todos/home.html', {
        'todos': todos
    })

def about_page(request):
    return render(request, 'todos/about.html')

def create_todo(request):
    # print(request.POST)
    Todo.objects.create(title=request.POST['title'])
    return redirect('home')

def complete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_completed = True
    todo.save()
    return redirect('home')

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('home')
