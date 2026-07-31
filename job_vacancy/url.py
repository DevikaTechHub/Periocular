from django.conf.urls import url
from job_vacancy import views

urlpatterns = [
    url('job_vacancy/',views.job_vacancy),
    url('jobv/',views.view_jbv.as_view()),

]