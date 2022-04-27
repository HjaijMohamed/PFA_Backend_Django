from django.conf.urls import url 
from personnels import views 
 
urlpatterns = [ 
    url(r'^api/personnels$', views.personnel_list),
    url(r'^api/personnels/(?P<cin>[0-9]+)$', views.personnel_detail),
]