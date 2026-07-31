from django.http import HttpResponse
from django.shortcuts import render
from complaint.models import Complaint
# Create your views here.(
def a_view_complaint(request):
    obj=Complaint.objects.all()
    context={
        'x':obj
    }
    return render(request,'complaint/authority_view_complaint.html',context)



def or_vw_reply(request):
    obj=Complaint.objects.all()
    context={
        'vv':obj
    }
    return render(request, 'complaint/org_vie_complaint_reply.html',context)



def post_reply(request,idd):
    if request.method == 'POST':
        obj = Complaint.objects.get(complaint_id=idd)
        obj.reply=request.POST.get('rp')
        obj.save()
    return render(request,'complaint/post reply.html')



def view_complaint(request):
    obj=Complaint.objects.all()
    context={
        'x':obj
    }
    return render(request,'complaint/view_complaint.html',context)



def  view_complaint_organisation(request):
    obj=Complaint.object.all()
    context={
        'x':obj
    }
    return render(request,'complaint/view_complaint organisation.html',context)






from rest_framework.views import APIView,Response
from acknowlegment.serializers import android_serializer
import datetime

class post_cmp(APIView):
    def post(self, request):
        ob = Complaint()
        ob.user_id = 1
        ob.date = datetime.datetime.today()
        ob.time = datetime.datetime.now()
        ob.complaint=request.data['complaint']
        ob.reply = "Pending"
        ob.save()
        HttpResponse('yes')




class view_cmp(APIView):
    def get(self,request):
        ob=Complaint.objects.all()
        ser=android_serializer(ob,many=True)
        return Response(ser.data)













