from django.conf.urls import url 
from absences import views 
 
urlpatterns = [ 
    url(r'^api/absences$', views.absence_list),
    url(r'^api/absences/(?P<pk>[0-9]+)$', views.absence_detail),
    url(r'^api/absenceAujourdhui$', views.absence_aujourdhui),

    
]