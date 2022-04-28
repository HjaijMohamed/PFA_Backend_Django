from django.conf.urls import url 
from presence import views 
 
urlpatterns = [ 
    url(r'^api/presences$', views.presence_list),
    url(r'^api/presences/(?P<cin>[0-9]+)/(?P<date>[\w\-]+)$', views.presence_detail),
    url(r'^api/recognition$', views.recognition),
    url(r'^api/recognitionOff$', views.recognitionOff),
    url(r'^api/presenceAujourdhui$', views.presence_aujourdhui),
    url(r'^api/retardAujourdhui$', views.retard_aujourdhui),
    
]