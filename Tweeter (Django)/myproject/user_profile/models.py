from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=200, blank=True)
    address = models.CharField(max_length=100, blank=True)
    nationality = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"