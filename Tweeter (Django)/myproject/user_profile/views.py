from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def view_profile(request, user_id):
    user = User.objects.get(id=user_id)
    profile, created = UserProfile.objects.get_or_create(user=user)
    if created:
        profile.save()
    return render(request, 'view_profile.html', {'profile': profile})

@login_required
def edit_profile(request, user_id):
    user = User.objects.get(id=user_id)
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile', user_id=user_id)
    else:
        UserProfileForm(instance=profile)
        form = UserProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})
