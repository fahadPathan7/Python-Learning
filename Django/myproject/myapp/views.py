from django.shortcuts import render

# Create your views here.
def myapp(request):
    return render(request, 'myapp/myapp.html')

def order(request):
    return render(request, 'myapp/order.html')