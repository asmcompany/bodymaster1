from importlib.resources import path

from my_acount.views import login_user, register

from django.urls import path, include




urlpatterns = [

    path('login', login_user),
    path('register', register )
]