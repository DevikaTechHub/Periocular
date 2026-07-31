from django.http import HttpResponse
from django.shortcuts import render
from user.models import User
# Create your views here.

def manage_user(request):
    ss=request.session["uid"]
    obj=User.objects.filter(user_id=ss)
    context={
        'x':obj
    }
    return render(request,'user/manage_user.html',context)



def approve(request,idd):
    obj=User.objects.get(user_id=idd)
    obj.status="Approved"
    return manage_user(request)


def reject(request,idd):
    obj=User.objects.get(user_id=idd)
    obj.status="Rejected"
    return manage_user(request)





from rest_framework.views import APIView,Response
from acknowlegment.serializers import android_serializer


class post_usp(APIView):
    def post(self, request):
        ob = User()
        ob.name= request.data['name']
        ob.email = request.data['email']
        ob.password = request.data['password']
        ob.phone_no = request.data['phone_no']
        ob.house_name=request.data['house_name']
        ob.place= request.data['place']
        ob.pin_code = request.data['pin_code']
        ob.save()
        return HttpResponse('yes')