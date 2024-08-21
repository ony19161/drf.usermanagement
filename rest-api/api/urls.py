from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_home),
    path('sign-up', views.sign_up, name='sign_up'),
    path('sign-in', views.sign_in, name='sign_in'),
    path('users', views.list_users, name='list_users'),
    path('users/add', views.add_user, name='add_user'),
    path('users/update/<int:user_id>', views.update_user, name='update_user'),
    path('users/delete/<int:user_id>', views.delete_user, name='delete_user'),
]
