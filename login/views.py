from django.http import HttpResponseRedirect
from django.shortcuts import render
from login.models import Login

# Create your views here.


def login(request):
    if request.method=='POST':
        name = request.POST.get("us")
        password = request.POST.get("ps")
        obj = Login.objects.filter(user_name=name,password=password)
        tp=""
        for ob in obj:
            tp= ob.type
            uid=ob.u_id
            if tp=="admin":
                request.session["uid"]=uid
                return HttpResponseRedirect('/temp/admin/')
            elif tp=="authority":
                request.session["uid"] = uid
                return HttpResponseRedirect('/temp/authority/')
            elif tp=="organaisation":
                request.session["uid"] = uid
                return HttpResponseRedirect('/temp/organisation/')
        else:
            objilist= "incorect username or password... please try again..!"
            context={
                "msg": objilist,
            }
            return render(request,'login/login.html',context)
    return render(request,'login/login.html')





