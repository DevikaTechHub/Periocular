from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from application.models import Application
from cert_details.models import CertDetails
# Create your views here.

def app(request):
    obb=CertDetails.objects.all()
    context={
        'a':obb
    }
    if request.method=='POST':
        obj=Application()
        obj.user_id=1
        obj.cert_details_id=request.POST.get('ce')
        # obj.rules=request.POST.get('rl')
        myfile=request.FILES['rl']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.rules=myfile.name

        obj.status=("pending")
        obj.save()
    return render(request,'application/post details application.html',context)



def vapp(request):
    obj=Application.objects.all()
    context={
        'x':obj
    }
    return render(request,'application/view_application.html',context)