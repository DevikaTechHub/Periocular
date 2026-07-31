from django.conf.urls import url
from complaint import views

urlpatterns = [
    url('auth_vw_complaint/',views.a_view_complaint),
    url('org_r/',views.or_vw_reply),
    url('reply/(?P<idd>\w+)',views.post_reply),
    url('view/',views.view_complaint),
    url('orgview/',views.view_complaint_organisation),
    url('comp/',views.post_cmp.as_view()),
    url('comv/',views.view_cmp.as_view()),

]