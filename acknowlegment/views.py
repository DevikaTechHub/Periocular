from django.http import HttpResponse
from django.shortcuts import render
from acknowlegment.models import Acknowledgment
import datetime
from user.models import User
# Create your views here.

def ack(request):
    obb=User.objects.all()
    context={
        'a':obb
    }
    if request.method=='POST':
        obj=Acknowledgment()
        obj.user_id=request.POST.get('us')
        obj.acknowledgment=request.POST.get('ac')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.save()
    return render(request,'acknowlegment/send aknowledgement to user.html',context)



def vack(request):
    obj=Acknowledgment.objects.all()
    context={
        'x':obj
    }
    return render(request,'acknowlegment/view_acknowlegment.html',context)



from rest_framework.views import APIView,Response
from acknowlegment.serializers import android_serializer



class view_ack(APIView):
    def get(self,request):
        ob=Acknowledgment()
        ser=android_serializer(ob,many=True)
        return Response(ser.data)

#
# class post_ack(APIView):
#     def post(self,request):
#         ob=Acknowledgment()
#         ob.user=request.data['user']
#         ob.acknowledgment=request.data['']
#         ob.save()
#         HttpResponse('yes')