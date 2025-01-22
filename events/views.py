from django.shortcuts import render
from .models import *
# Create your views here.
def view_events(request):
    query_set = events.objects.all()
    workshops = query_set.filter(type='Workshop')
    competitions = query_set.filter(type='Competition')
    if_workshops = workshops.exists()
    if_competitions = competitions.exists()
    print(if_workshops)
    return render(request, 'events.html', context={
        'if_workshops': if_workshops,
        'workshops': workshops,
        'if_competitions': if_competitions,
        'competitions': competitions,
    })
