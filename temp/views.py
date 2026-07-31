from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'temp/home.html')


def admin(request):
    return render(request,'temp/admin.html')

def authority(request):
    return render(request,'temp/authority.html')

def organisation(request):
    return render(request,'temp/organisation.html')

def mhome(request):
    return render(request,'temp/mhome.html')

def madmin(request):
    return render(request, 'temp/madmin.html')

def mauthority(request):
    return render(request,'temp/mauthority.html')

def morg(request):
    return render(request,'temp/morg.html')