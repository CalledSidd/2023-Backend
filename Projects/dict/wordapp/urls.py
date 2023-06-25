from django.urls import path
from .views import Word
urlpatterns = [
    path('',Word.as_view())
]
