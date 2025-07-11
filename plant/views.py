from django.shortcuts import render
from .models import tips

# Create your views here.
def home(request):
    tips_info=tips.objects.all()
    #print(tips_info)
    return render(request,'plant/home.html',{'tips_info':tips_info})

def explore(request):
    return render(request,'plant/explore.html')

def myplants(request):
    return render(request,'plant/myplants.html')

def addplant(request):
    return render(request,'plant/addplant.html')