from django.conf.urls import url
from job_application import views

urlpatterns = [

    url('view/',views.v_job_application),
    url('select/(?P<idd>\w+)',views.v_job_application),
    url('jav/',views.view_jbav.as_view()),

]