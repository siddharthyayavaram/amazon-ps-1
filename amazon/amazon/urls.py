from django.contrib import admin
from django.urls import include, re_path, path
from shipparams.api import Shiplist, Shipcost

urlpatterns = [
    path('', include('shipparams.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^api/ships_list/$', Shiplist.as_view(), name='ship_list'),
    re_path(r'^api/ships_list/(?P<id>\d+)/$', Shipcost.as_view(), name='ship_cost'),
]
