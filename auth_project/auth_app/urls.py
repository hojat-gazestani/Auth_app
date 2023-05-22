from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.auth_root, name='auth_root'),
    path('auth1/', views.auth1, name='auth1'),
    path('auth2/', views.auth2, name='auth2'),
]
