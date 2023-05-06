from django.urls import path

from . views import (
    IndexView
)


urlpatterns = [
    PATH('', IndexView.as_view(), name='index' )
]
