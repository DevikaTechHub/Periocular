from django.conf.urls import url
from cert_request import views

urlpatterns = [
    url('cert_request/',views.c_request),
    url('crv/',views.view_cereq.as_view()),
    url('crp/',views.view_cereq.as_view()),
]