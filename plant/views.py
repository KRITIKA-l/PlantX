from django.shortcuts import render, get_object_or_404, redirect
from .models import tips,plantinfo,userplant
import markdown
from .forms import UserPlantForm
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    tips_info=tips.objects.all()
    #print(tips_info)
    return render(request,'plant/home.html',{'tips_info':tips_info})

def explore(request):
    plants = plantinfo.objects.all()
    return render(request, 'plant/explore.html', {'plants': plants})

def plantdetails(request, plant_id):
    plant = get_object_or_404(plantinfo, plant_id=plant_id)
    processed_plants = {
        'plant_id': plant.plant_id,
        'name': plant.plant_name,
        'image': plant.plant_img,
        'content': markdown.markdown(plant.plant_desc)
    }
    return render(request, 'plant/plantinfo.html', {'plant': processed_plants})

@login_required(login_url='loginuser')
def addplant(request):
    if request.method == 'POST':
        form = UserPlantForm(request.POST, request.FILES)
        if form.is_valid():
            plant = form.save(commit=False)
            plant.user = request.user
            plant.save() 
            return redirect('myplants')
    else:
        form = UserPlantForm() 
    return render(request, 'plant/addplant.html', {'form': form})

@login_required(login_url='loginuser')
def myplants(request):
    user_plant = userplant.objects.all().filter(user=request.user)
    return render(request, 'plant/myplants.html', {'userplant': user_plant})

@login_required
def myplantinfo(request, userplant_id):
    plant = get_object_or_404(userplant, id=userplant_id, user=request.user)
    return render(request, 'plant/myplantinfo.html', {'plant': plant})

def loginuser(request):
    if request.method=='GET':
        return render(request,'plant/loginuser.html')
    else:
        a=request.POST.get('username')
        b=request.POST.get('password')
        user=authenticate(request,username=a,password=b)
        if user is None:
            return render(request,'plant/loginuser.html',{'error':'Invalid Credentials!'})
        else:
            login(request,user)
            return (redirect('home'))

def signupuser(request):
    if request.method=='GET':
        return render(request,'plant/signupuser.html')
    else:
        a=request.POST.get('username')
        b=request.POST.get('password1')
        c=request.POST.get('password2')
        if(b==c):
            if(User.objects.filter(username=a).exists()):
                return render(request,'plant/signupuser.html',{'error':'User Already Exists!'})
            else:
                user=User.objects.create_user(username=a,password=b)
                user.save()
                login(request,user)
                return (redirect('home'))
        else:
            return render(request,'plant/signupuser.html',{'error':'Password Mismatched!'})
        
def logoutuser(request):
    if request.method=='GET':
        logout(request)
        return(redirect('home'))