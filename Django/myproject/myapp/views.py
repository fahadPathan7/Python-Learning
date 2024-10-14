from django.shortcuts import render
from .models import ChaVarity, Store
from django.shortcuts import get_object_or_404
from .forms import ChaVarityForm

# Create your views here.
def myapp(request):
    all_tea = ChaVarity.objects.all()
    return render(request, 'myapp/myapp.html', {'all_tea': all_tea})

def cha_description(request, cha_id):
    cha = get_object_or_404(ChaVarity, id=cha_id)
    return render(request, 'myapp/chaDetails.html', {'cha': cha})

def order(request):
    return render(request, 'myapp/order.html')

def chaShops(request):
    stores = None
    if request.method == 'POST':
        form = ChaVarityForm(request.POST)
        if form.is_valid():
            cha_varity = form.cleaned_data['cha_varity']
            stores = Store.objects.filter(cha_variety=cha_varity)
    else:
        form = ChaVarityForm() # This will create a dropdown list of all the cha varieties.
    return render(request, 'myapp/chaStores.html', {'stores': stores, 'form': form})