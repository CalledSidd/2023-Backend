from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views import View

from .models import Todo

# Create your views here.
class Index(TemplateView):
    template_name ='index.html'

class Todos(View):
    model = Todo
    template = 'todo/todo.html'
    def get(self, request):
        todo_items = self.model.objects.all()
        print(todo_items)
        context = {
            'todos' : todo_items,
        }
        return render(request,self.template, context)
    def post(self, request):
        title = request.POST.get('title')
        if title:
            todo = Todo.objects.create(title = title)
            return redirect(Todos)
    def put(self, request):
        pass