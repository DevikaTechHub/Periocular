from django.shortcuts import render
from cert_request.models import CertRequest
# Create your views here.
def c_request(request):
    obj=CertRequest.objects.all()
    context={
        'x':obj
    }
    return render(request,'cert_request/view_certificate_request.html',context)


from rest_framework.views import APIView, Response
from cert_request.serializers import android_serializer


class view_cereq(APIView):
    def get(self, request):
        ob = CertRequest()
        ser = android_serializer(ob, many=True)
        return Response(ser.data)


class post_cereq(APIView):
     def post(self,request):
         ob=CertRequest()
         ob.cert_request_id=request.data['cert_request_id']
         ob.user_id=request.data['user_id']
         ob.date = request.data['date']
         ob.time = request.data['time']
         ob.save()
         HttpResponse('yes')

