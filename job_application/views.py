from django.shortcuts import render
from job_application.models import JobApplication

# Create your views here.



def v_job_application(request):
    obj=JobApplication.objects.all()
    context={
        'x':obj
    }
    return render(request,'job_application/view_job_application and select.html',context)



def select(request,idd):
    obj=JobApplication.objects.get(feature_id=idd)
    obj.status="Selected"
    obj.save()
    return v_job_application(request)





from rest_framework.views import APIView,Response
from job_application.serializers import android_serializer




class view_jbav(APIView):
    def get(self,request):
        ob=JobApplication()
        ser=android_serializer(ob,many=True)
        return Response(ser.data)