from django.urls import path

from . views import (
    IndexView,
    LoginView,
    SignupView
)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/',LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
]
