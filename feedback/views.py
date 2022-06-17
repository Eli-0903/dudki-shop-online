import re
from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
# Create your views here.
def index(request):
    return render(request, 'feedback/index.html')
    
def create(request):
    if request.method == "POST":
        full_name = request.POST["Full_name"]
        bio = request.POST["bio"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        
        new_profile = Profile(full_name= full_name, bio = bio, email = email, phone = phone)
        new_profile.save()
        success = "Profile Created Successfully for " + full_name
        return HttpResponse(success)