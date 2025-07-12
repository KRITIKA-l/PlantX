from django.shortcuts import render, get_object_or_404
from .models import tips,plantinfo
import markdown

# Create your views here.
def home(request):
    tips_info=tips.objects.all()
    #print(tips_info)
    return render(request,'plant/home.html',{'tips_info':tips_info})

def explore(request):
    plants = plantinfo.objects.all()
    return render(request, 'plant/explore.html', {'plants': plants})

def myplants(request):
    return render(request,'plant/myplants.html')

def addplant(request):
    return render(request,'plant/addplant.html')

def plantdetails(request, plant_id):
    plant = get_object_or_404(plantinfo, plant_id=plant_id)
    processed_plants = {
        'plant_id': plant.plant_id,
        'name': plant.plant_name,
        'image': plant.plant_img,
        'content': markdown.markdown(plant.plant_desc)
    }
    return render(request, 'plant/plantinfo.html', {'plant': processed_plants})