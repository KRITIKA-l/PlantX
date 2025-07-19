from django.shortcuts import render, get_object_or_404, redirect
from .models import tips,plantinfo,userplant,userprofile
import markdown
from .forms import UserPlantForm
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from django.conf import settings
import requests 

# Create your views here.
def home(request):
    tips_info=tips.objects.all()
    #print(tips_info)
    return render(request,'plant/home.html',{'tips_info':tips_info})

def explore(request):
    plants = plantinfo.objects.all()
    paginator = Paginator(plants, 3)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'plant/explore.html', {"page_obj": page_obj})

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
    return render(request, 'plant/myplants.html')

@login_required(login_url='loginuser')
def navbar(request):
    return render(request, 'plant/navbar.html')

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
        d=request.POST.get('city')
        if(b==c):
            if(User.objects.filter(username=a).exists()):
                return render(request,'plant/signupuser.html',{'error':'User Already Exists!'})
            else:
                user=User.objects.create_user(username=a,password=b)
                user.save()
                userprofile.objects.create(user=user, user_city=d, password=b)
                login(request,user)
                return (redirect('home'))
        else:
            return render(request,'plant/signupuser.html',{'error':'Password Mismatched!'})
        
def logoutuser(request):
    if request.method=='GET':
        logout(request)
        return(redirect('home'))
    
def findproducts(request):
    if request.method == 'POST':
        x = request.POST.get('prod_search', '')
        tipsdata = tips.objects.filter(Q(tip_name__icontains=x) | Q(tip_desc__icontains=x))
        plantdata = plantinfo.objects.filter(Q(plant_name__icontains=x))
        userdata = userplant.objects.filter(Q(nickname__icontains=x) | Q(notes__icontains=x))
        tips_info=tips.objects.all()
        if x:
            return render(request, 'plant/search.html', {
                'tipsdata': tipsdata,
                'plantdata': plantdata,
                'userdata': userdata,
            })
        elif x == '':
            return render(request,'plant/home.html',{'tips_info':tips_info})
        else:
            return render(request, 'plant/search.html', {'warning': "No Record Found"})
        
@login_required
def notifications(request):
    user_profile = userprofile.objects.get(user=request.user)
    city = user_profile.user_city

    api_key = settings.OPENWEATHER_API_KEY
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)
    weather_data = response.json()

    weather_main = weather_data['weather'][0]['main'] 
    temp = weather_data['main']['temp']

    context = {
        'user': request.user,
        'city': city,
        'weather': {
            'main': weather_main,
            'temp': temp,
        }
    }
    return render(request, 'plant/notifications.html', context)

@login_required
def profile(request):
    profile = get_object_or_404(userprofile, user=request.user)

    if request.method == 'POST':
        profile.user_email = request.POST.get('user_email')
        profile.user_city = request.POST.get('user_city')
        if 'user_dp' in request.FILES:
            profile.user_dp = request.FILES['user_dp']
        profile.save()

    return render(request, 'plant/profile.html', {
        'user': request.user,
        'profile': profile
    })