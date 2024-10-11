from django.urls import path
from . import views

urlpatterns = [
    path('', views.myapp, name='myapp'),
    path('order/', views.order, name='order'),
]