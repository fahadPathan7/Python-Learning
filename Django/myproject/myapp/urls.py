from django.urls import path
from . import views

urlpatterns = [
    path('', views.myapp, name='myapp'),
    path('order/', views.order, name='order'),
    path('<int:cha_id>/', views.cha_description, name='cha_description'),
]