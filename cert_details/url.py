from django.conf.urls import url
from cert_details import views

urlpatterns = [
    url('cert_details/',views.c_details),
    url('vcd/',views.view_cerdet.as_view()),

]