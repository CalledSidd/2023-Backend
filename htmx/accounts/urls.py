from django.urls import path
from accounts.views import (
    IndexView,
    Login,
    RegisterView,
    check_username
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index/',IndexView.as_view(), name='index'),
    path('login/',Login.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('register/',RegisterView.as_view(), name='register'),
]

htmx_views = [
    path('check_username/', check_username, name='check_username')
]

urlpatterns += htmx_views
