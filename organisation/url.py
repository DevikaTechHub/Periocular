from django.conf.urls import url
from organisation import views

urlpatterns = [
    url('vwup/',views.organisation),
    # url('vwup/',views.up_organisation),
    url('org/',views.org),
    url('update/(?P<idd>\w+)',views.up_organisation),
    url('delete/(?P<idd>\w+)', views.delete)


]