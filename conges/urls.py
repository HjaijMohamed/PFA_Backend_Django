from django.conf.urls import url 
from conges import views 
 
urlpatterns = [ 
    url(r'^api/conges$', views.conge_list),
    url(r'^api/conges/(?P<pk>[0-9]+)$', views.conge_detail),
    url(r'^api/congeAujourdhui$', views.conge_aujourdhui),

]