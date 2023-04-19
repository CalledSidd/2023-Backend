from django.urls import path
from django.views.generic import TemplateView, RedirectView
from . views import Ex2View

app_name = 'core'

urlpatterns = [
    path('ex1', TemplateView.as_view(template_name='ex1.html', 
                                            extra_context={'title':'Template Class Based View'})),
    path('ex2',Ex2View.as_view(), name = 'ex2'),
    path('rdt',RedirectView.as_view(url = 'https://www.youtube.com/channel/UCCiV8Ht-AJZlc2VnA-MNu_Q'), name = 'go-to-google'),
    path('ex3/<int:pk>/', PostPreLoadTaskView.as_view(), name='redirect-task'),
]
