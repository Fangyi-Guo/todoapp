from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo, StickyNote

# Create your views here.
def index(request):
    notes = StickyNote.objects.all()
    #mass_todos = Todo.objects.all()
    #todos = []
    #for note in notes:
    #    note_todos = note.note_set.all()
    #    for todo in note_todos:
    #        todos[note.id][todo.id] = todo
    context = {
        'notes':notes,
        #'todos':todos
    }
    return render(request, 'index.html', context)

def details(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo':todo 
    }
    return render(request, 'details.html', context)

def add(request,id):
    note = StickyNote.objects.get(id=id)
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']
        todo = Todo(title=title, text=text, note=note)
        todo.save()
        return redirect('/todos')
    return render(request, 'add.html', {'note':note})

def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/todos')

def Note(request):
    if(request.method == 'POST'):
        name = request.POST['note_name']
        note = StickyNote(note_name=name)
        note.save()
        return redirect('/todos')
    else:
        return render(request, 'addNote.html')

def removeNote(request, id):
    note = StickyNote.objects.get(id=id)
    note.delete()
    return redirect('/todos')