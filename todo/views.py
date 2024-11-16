from django.http import JsonResponse
from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        new_task = Task.objects.create(title=title)
        return JsonResponse({'id': new_task.id, 'title': new_task.title})

def update_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('id')
        completed = request.POST.get('completed') == 'true'
        task = Task.objects.get(id=task_id)
        task.completed = completed
        task.save()
        return JsonResponse({'id': task.id, 'completed': task.completed})
    