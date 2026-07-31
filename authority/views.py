from django.shortcuts import render
from authority.models import Authority
from login.models import Login
# Create your views here.


def authority(request):
    if request.method=='POST':
        obj=Authority()
        obj.password=request.POST.get('pa')
        obj.email=request.POST.get('em')
        obj.phone_no=request.POST.get('nu')
        obj.name=request.POST.get('na')
        obj.location=request.POST.get('lo')
        obj.save()
        ob=Login()
        ob.user_name=obj.name
        ob.password=obj.password
        ob.type='authority'
        ob.u_id=1
        ob.save()
    return render(request,'authority/authority.html')



def up_authority(request,idd):
    obb=Authority.objects.get(authority_id=idd)
    context={
        'aa':obb
    }
    if request.method=='POST':
        obj=Authority.objects.get(authority_id=idd)
        obj.name=request.POST.get('nm')
        obj.email=request.POST.get('em')
        obj.password=request.POST.get('ps')
        obj.phone_no=request.POST.get('ph')
        obj.location=request.POST.get('lc')
        obj.save()
        return v_authority(request)
    return render(request,'authority/authority update profile.html',context)

def delete(request,idd):
    obj=Authority.objects.get(authority_id=idd)
    obj.delete()
    return v_authority(request)

def v_authority(request):
    ss=request.session["uid"]
    obj=Authority.objects.filter(authority_id=ss)
    context={
        'x':obj
    }
    return render(request,'authority/view_and_update_profile.html',context)


from rest_framework.views import APIView, Response
from authority.serializers import android_serializer


class view_auth(APIView):
    def get(self, request):
        ob = Authority()
        ser = android_serializer(ob, many=True)
        return Response(ser.data)
