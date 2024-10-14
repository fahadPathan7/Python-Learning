from django.shortcuts import render
from .models import ChaVarity
from django.shortcuts import get_object_or_404

# Create your views here.
def myapp(request):
    all_tea = ChaVarity.objects.all()
    return render(request, 'myapp/myapp.html', {'all_tea': all_tea})

def cha_description(request, cha_id):
    cha = get_object_or_404(ChaVarity, id=cha_id)
    return render(request, 'myapp/chaDetails.html', {'cha': cha})

def order(request):
    return render(request, 'myapp/order.html')