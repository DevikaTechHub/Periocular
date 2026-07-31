from django.conf.urls import url
from feature import views


urlpatterns = [
    url('feature/',views.feature),
    url('manage/',views.manage_feature),
    url('edit/(?P<idd>\w+)',views.edit),
    url('delete/(?P<idd>\w+)',views.delete)

]