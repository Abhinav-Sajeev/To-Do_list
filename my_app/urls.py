from django.urls import path
from .import views



urlpatterns = [
    path('index/',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('',views.login,name='login'),
    path('display/',views.display,name='display'),
    path('items/<int:pk>/delete',views.delt,name='delete'),
    path('edit/<int:pk>/', views.edit, name='edit'),
]