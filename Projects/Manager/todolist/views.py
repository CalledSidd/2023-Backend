from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View

# Create your views here.
class Index(TemplateView):
    template_name ='index.html'

class Todo(View):
    template = 'todo/todo.html'
    def get(self, request):
        return render(request, self.template)