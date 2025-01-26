from django.shortcuts import render
from .models import *
import itertools
def group_in_chunks(data, n):
    data = list(data)
    return [data[i:i + n] for i in range(0, len(data), n)]
# Create your views here.
def view_univ(request):
    country=""
    fields=[]
    if request.method=="POST":
        country = request.POST.get("country", "")
        fields = request.POST.getlist("field")
        if len(fields)==0 or country=="":
            return render(request,'./index.html', context={'data':False,'country':country,'fields':fields})
        data=ranks.objects.filter(country=country,topic=fields[0]).select_related('name').values(
            'name__name',
            'name__img',
            'name__location',
            'name__acceptance',
            'name__gre',
            'score'
        )
        query_data=group_in_chunks(data, 4)
        print(len(query_data))
        print(len(data))
        context={
            'data':True,
            'query':query_data,
            'country':country,
            'fields':fields
        }
        return render(request,'./index.html',context=context)
    return render(request,'./index.html', context={'data':False,'country':country,'fields':fields})