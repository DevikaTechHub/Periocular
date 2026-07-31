from django.shortcuts import render
from cert_details.models import CertDetails
# Create your views here.
def c_details(request):
    if request.method=='POST' :
        obj=CertDetails()
        obj.name=request.POST.get('nm')
        obj.description=request.POST.get('ds')
        obj.type=request.POST.get('tp')
        obj.save()
    return render(request,'cert_details/certificate.html')


from rest_framework.views import APIView, Response
from cert_details.serializers import android_serializer


class view_cerdet(APIView):
    def get(self, request):
        ob = CertDetails()
        ser = android_serializer(ob, many=True)
        return Response(ser.data)
