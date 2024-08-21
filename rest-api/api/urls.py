from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_home),
    path('sign-up', views.sign_up, name='sign_up'),
]
