from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.oferta_list, name='oferta_list'), #oferta_list jest defaultowo włączana jako strona głowna
]