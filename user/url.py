from django.conf.urls import url
from user import views

urlpatterns = [
    url('user/',views.manage_user),
    url('approve/(?P<idd>\w+)',views.approve),
    url('reject/(?P<idd>\w+)',views.reject),
    url('usrp/',views.post_usp.as_view()),

]