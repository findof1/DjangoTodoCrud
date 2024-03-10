from django.shortcuts import render
import json
from django.http import JsonResponse
from django.urls import reverse
from .models import Todo
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def test(res):
  return JsonResponse({'test':'test'})

@csrf_exempt
def todos(request):
  todos = Todo.objects.all()
  todos_list = serializers.serialize('json', todos)
  return JsonResponse(todos_list, safe=False)



@csrf_exempt
def add_todo(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            todo_name = data.get('todo_name')
            if todo_name:
                Todo.objects.create(todo_name=todo_name)
                todos = Todo.objects.all()
                todos_list = serializers.serialize('json', todos)
                return JsonResponse(json.loads(todos_list), safe=False)
            else:
                return JsonResponse({'error': 'todo_name field is missing'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def delete_todo(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            id = int(data.get('id'))
            if id:
                todo = Todo.objects.get(id=id)
                todo.delete()
                todos = Todo.objects.all()
                todos_list = serializers.serialize('json', todos)
                return JsonResponse(json.loads(todos_list), safe=False)
            else:
                return JsonResponse({'error': 'field is missing'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error', 'invalid json'}, status=400)
        except Todo.DoesNotExist:
            return JsonResponse({'error': 'Todo with the given ID does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def setComplete(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id = int(data.get('id'))
            if id:
                todo = Todo.objects.get(id=id)
                todo.completed = True
                todo.save()
                todos = Todo.objects.all()
                todos_list = serializers.serialize('json', todos)
                return JsonResponse(json.loads(todos_list), safe=False)
            else:
                return JsonResponse({'error': 'field is missing'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error', 'invalid json'}, status=400)
        except Todo.DoesNotExist:
            return JsonResponse({'error': 'Todo with the given ID does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def setNotComplete(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id = int(data.get('id'))
            if id:
                todo = Todo.objects.get(id=id)
                todo.completed = False
                todo.save()
                todos = Todo.objects.all()
                todos_list = serializers.serialize('json', todos)
                return JsonResponse(json.loads(todos_list), safe=False)
            else:
                return JsonResponse({'error': 'field is missing'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error', 'invalid json'}, status=400)
        except Todo.DoesNotExist:
            return JsonResponse({'error': 'Todo with the given ID does not exist'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)