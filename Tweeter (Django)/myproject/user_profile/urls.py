from django.db import models
from django.contrib.auth.models import User
from django.urls import path, include
from . import views

urlpatterns = [
    path('view/<int:user_id>/', views.view_profile, name='view_profile'),
    path('edit/<int:user_id>/', views.edit_profile, name='edit_profile'),
]
