from django.urls import path
from . import views

urlpatterns = [
    path('shipparams/', views.shipparams, name='shipparams'),
]