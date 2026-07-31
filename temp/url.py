from django.conf.urls import url
from temp import views


urlpatterns=[
    url('home/',views.home),
    url('admin/',views.admin),
    url('authority/',views.authority),
    url('organisation/',views.organisation),
    url('mhm/',views.mhome),
    url('ma/',views.madmin),
    url('matho/',views.mauthority),
    url('morga/',views.morg)
]