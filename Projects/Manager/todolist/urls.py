from django.urls import path

from . views import (
    Index,
    Todo,
)



urlpatterns =[
    path('', Todo.as_view(), name='list'),
]