from django.shortcuts import render
from .models import blogs
# Create your views here.
def view_blogs(request):
    # blogs.objects.all().delete()
    query_set=blogs.objects.all()
    print(query_set)
    return render(request,'blogs.html',context={'query':query_set})