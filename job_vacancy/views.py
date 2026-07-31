from django.shortcuts import render
from job_vacancy.models import JobVacancy
import datetime
# Create your views here.

def job_vacancy(request):
    if request.method=='POST':
        obj=JobVacancy()
        obj.company=request.POST.get('co')
        obj.designation=request.POST.get('de')
        obj.date=datetime.datetime.now()
        obj.time=datetime.datetime.now()
        obj.qualification=request.POST.get('qu')
        obj.save()
    return render(request,'job_vacancy/job vaccancies.html')


from rest_framework.views import APIView, Response
from job_vacancy.serializers import android_serializer


class view_jbv(APIView):
    def get(self, request):
        ob = JobVacancy()
        ser = android_serializer(ob, many=True)
        return Response(ser.data)
