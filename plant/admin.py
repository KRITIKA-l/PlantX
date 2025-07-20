from django.contrib import admin
from .models import tips,plantinfo,userplant,userprofile,planthistory
# Register your models here.

admin.site.register(tips)
admin.site.register(plantinfo)
admin.site.register(userplant)
admin.site.register(userprofile)
admin.site.register(planthistory)