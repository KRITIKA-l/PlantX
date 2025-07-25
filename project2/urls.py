"""
URL configuration for project2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path
from plant import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('explore',views.explore,name='explore'),
    path('plant/<str:plant_id>/', views.plantdetails, name='plantdetails'),

    path('navbar',views.navbar,name='navbar'),
    path('myplants',views.myplants,name='myplants'),
    path('myplants/<int:userplant_id>/', views.myplantinfo, name='myplantinfo'),
    path('addplant',views.addplant,name='addplant'),

    path('loginuser/',views.loginuser,name='loginuser'),
    path('signupuser/',views.signupuser,name='signupuser'),
    path('logoutuser/',views.logoutuser,name='logoutuser'),

    path('findproducts',views.findproducts,name='findproducts'),
    path('notifications',views.notifications,name='notifications'),
    path('profile',views.profile,name='profile'),

    path('history/<int:userplant_id>/', views.history, name='history'),
    path('update-water/<int:plant_id>/', views.update_last_watered, name='update_last_watered'),
    path('update-fertilized/<int:plant_id>/', views.update_last_fertilized, name='update_last_fertilized'),
    path('plant/<int:plant_id>/update_custom_date/', views.update_custom_date, name='update_custom_date'),

    path('removeplant/<int:plant_id>/', views.removeplant, name='removeplant'),
    path('deletedplants/', views.deleted_plants, name='deleted_plants'),
    path('restoreplant/<int:plant_id>/', views.restoreplant, name='restoreplant'),
    path('editplant/<int:plant_id>/', views.editplant, name='editplant'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)