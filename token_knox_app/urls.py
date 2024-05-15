from django.urls import path
from . import views
from knox import views as knox_view

urlpatterns = [
    path('login', views.login_api),
    path('user', views.get_user_data),
    path('register', views.register_api),
    path('logout', knox_view.LogoutView.as_view()),
    path('logoutall', knox_view.LogoutAllView.as_view()),
]