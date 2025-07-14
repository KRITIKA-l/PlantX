from plant.models import userplant

def userplants_context(request):
    if request.user.is_authenticated:
        return {
            'userplant': userplant.objects.filter(user=request.user)
        }
    return {'userplant': None}
