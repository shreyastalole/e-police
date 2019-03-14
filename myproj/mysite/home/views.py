from django.http import HttpResponse
from django.shortcuts import render
from .models import details

def index(request):
    all_details = details.objects.all()
    context ={'all_details':all_details}
    return render(request,'Home/home.html',context)
def detail(request, det_id):
    return HttpResponse("<h2>Details id: "+ str(det_id) + "</h2>")
