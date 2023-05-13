from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class TodoView(View):
    def get(self, request):
        pass
    def post(self, request):
        pass
    def delete(self, request):
        pass
    def put(self, request):
        pass