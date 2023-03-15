from django.urls import path
from .views import LoginView,SiginView,TestUser
urlpatterns = [
    path('',LoginView.as_view()),
    path('signin/',SiginView.as_view()),
    path('test/',TestUser.as_view())
]