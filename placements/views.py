from django.shortcuts import render

# Create your views here.
def view_main_placements(request):
    return render(request,'./placement.html')