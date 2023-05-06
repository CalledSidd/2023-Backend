from django.urls import path

from . views import (
    IndexView,
    LoginView,
    SignupView,
    LogoutView
)
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(IndexView.as_view()), name='index'),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/', LogoutView, name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
]
