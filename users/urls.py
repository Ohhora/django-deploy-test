from django.urls import path, include
from django.contrib.auth import views as auth_views

app_name = "users"
urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]
