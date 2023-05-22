from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View

from .models import Todo

# Create your views here.
class Index(TemplateView):
    template_name ='index.html'

class Todos(View):
    template = 'todo/todo.html'
    def get(self, request):
        todos = Todo
        context = {
            todos : 'todos'
        }
        return render(request, self.template, context)
    def post(self, request):
        pass
    def put(self, request):
        pass