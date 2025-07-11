from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'plant/home.html')

def explore(request):
    return render(request,'plant/explore.html')

def myplants(request):
    return render(request,'plant/myplants.html')