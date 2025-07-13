from django.shortcuts import render, get_object_or_404, redirect
from .models import tips,plantinfo,userplant
import markdown
from .forms import UserPlantForm

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
    if request.method == 'POST':
        form = UserPlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('myplants') 
    else:
        form = UserPlantForm() 
        return render(request, 'plant/addplant.html', {'form': form})

def plantdetails(request, plant_id):
    plant = get_object_or_404(plantinfo, plant_id=plant_id)
    processed_plants = {
        'plant_id': plant.plant_id,
        'name': plant.plant_name,
        'image': plant.plant_img,
        'content': markdown.markdown(plant.plant_desc)
    }
    return render(request, 'plant/plantinfo.html', {'plant': processed_plants})