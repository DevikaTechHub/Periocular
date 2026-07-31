from django.conf.urls import url
from application import views


urlpatterns=[
    url('application/',views.app),
    url('views/',views.vapp)
]