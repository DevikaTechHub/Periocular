from django.conf.urls import url
from authority import views

urlpatterns = [
    url('authority/',views.authority),
    url('update/(?P<idd>\w+)',views.up_authority),
    url('delete/(?P<idd>\w+)', views.delete),

    url('view/',views.v_authority),
    url('vath/',views.view_auth.as_view()),

]