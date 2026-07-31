from django.shortcuts import render
from feature.models import Feature
from authority.models import Authority
# Create your views here.
def feature(request):
    ss=request.session["uid"]
    obb=Authority.objects.all()
    context={
        'a':obb
    }
    if request.method=='POST':
        obj=Feature()
        obj.authority_id=ss
        obj.description=request.POST.get('ds')
        obj.features=request.POST.get('ft')
        obj.save()
    return render(request,'feature/feature.html',context)



def manage_feature(request):
    ss=request.session["uid"]
    obj=Feature.objects.filter(authority_id=ss)
    context={
        'x':obj
    }
    return render(request,'feature/manage_feature.html',context)



def edit(request,idd):
    obb=Feature.objects.get(feature_id=idd)
    context={
        'd':obb
    }
    if request.method=='POST':
        obj=Feature.objects.get(feature_id=idd)
        obj.features=request.POST.get('fet')
        obj.description=request.POST.get('des')
        obj.save()
        return manage_feature(request)
    return render(request,'feature/edit.html',context)


def delete(request,idd):
    obj=Feature.objects.get(feature_id=idd)
    obj.delete()
    return manage_feature(request)