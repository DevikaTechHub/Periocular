from django.shortcuts import render
from organisation.models import Organisation
from login.models import  Login
# Create your views here.

def organisation(request):
    ss=request.session["uid"]
    obj=Organisation.objects.filter(organisation_id=ss)
    context={
        'x':obj

    }
    return render(request,'organisation/organaisation update.html',context)


def up_organisation(request,idd):
    obb=Organisation.objects.get(organisation_id=idd)
    context={
        'a':obb
    }
    if request.method=='POST' :
        obj=Organisation.objects.get(organisation_id=idd)
        obj.name=request.POST.get('un')
        obj.email=request.POST.get('em')
        obj.password=request.POST.get('ps')
        obj.phone_no=request.POST.get('pn')
        obj.address = request.POST.get('ad')
        obj.save()
        return organisation(request)
    return render(request,'organisation/organaisation update profile.html',context)

def delete(request,idd):
    obj=Organisation.objects.get(organisation_id=idd)
    obj.delete()
    return organisation(request)


def org(request):
    if request.method=='POST':
        obj=Organisation()
        obj.name=request.POST.get('un')
        obj.password=request.POST.get('ps')
        obj.phone_no=request.POST.get('ph')
        obj.email=request.POST.get('em')
        obj.address=request.POST.get('ad')
        obj.save()
        ob = Login()
        ob.user_name = obj.name
        ob.password = obj.password
        ob.type = 'organaisation'
        ob.u_id = obj.organisation_id
        ob.save()
    return render(request,'organisation/organisation.html')


