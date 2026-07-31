from django.conf.urls import url
from acknowlegment import views


urlpatterns=[
    url('acknowlegement/',views.ack),
    url('viewack/',views.vack),

    url('va/',views.view_ack.as_view()),
]