"""urlconf for the base application"""

from django.conf.urls import url

from .views import * 


urlpatterns = [
    url(r'^ann/$', ANNView.as_view(), name='ann'),
    url(r'^kalman/$', KalmanView.as_view(), name='kalman'),
    url(r'^$', index, name='index'),
]