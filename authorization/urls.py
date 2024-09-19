from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('signup/', views.registration, name='signup'),
    path('login/', authViews.LoginView.as_view(template_name='authorization/login.html'), name='login'),
    path('exit/', authViews.LogoutView.as_view(template_name='authorization/exit.html'), name='exit'),
    path('user/', views.user_account, name='user'),
    path('user/links/', views.user_links, name='links'),
    path('user/settings/', views.user_settings, name='settings'),
    path('user/links/newlink/', views.user_newlink, name='newlink'),
]
