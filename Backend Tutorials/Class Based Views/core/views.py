from django.shortcuts import render
from django.views.generic.base import TemplateView
from core.models import Post

# Create your views here.
class Ex2View(TemplateView):
    template_name = 'ex2.html'
    # template_engine = Jinja2, Genshi 
    # response_class = w
    # content_type = 

    def get_context_data(seld, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.get(id = 1)
        context['data']  = "Context for Ex2"
        return context

