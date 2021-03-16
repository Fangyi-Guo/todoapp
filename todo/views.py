from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo, StickyNote

# Create your views here.
def index(request):
    notes = StickyNote.objects.all()[:10]
    
    context = {
        'notes':notes 
    }
    return render(request, 'index.html', context)

def details(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo':todo 
    }
    return render(request, 'details.html', context)

def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title=title, text=text)
        todo.save()
        return redirect('/todos')
    else:
        return render(request, 'add.html')

def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/todos')