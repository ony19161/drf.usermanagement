from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_home),
    path('sign-up', views.sign_up, name='sign_up'),
    path('users', views.list_users, name='list_users'),
]
