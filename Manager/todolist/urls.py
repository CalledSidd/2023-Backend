from django.urls import path

from . views import (
    Index,
    Todos,
)



urlpatterns =[
    path('', Todos.as_view(), name='list'),
]