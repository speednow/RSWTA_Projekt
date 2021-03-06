from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.oferta_list, name='oferta_list'), #oferta_list jest defaultowo włączana jako strona głowna
    url(r'^oferta/$', views.oferta_list, name='oferta_list'),  # oferta_list jest defaultowo włączana jako strona głowna
    url(r'^firma/$', views.firma_list, name='firma_list'),  # oferta_list jest defaultowo włączana jako strona głowna
    url(r'^oferta/(?P<pk>\d+)/$', views.oferta_detail, name='oferta_detail'),
]