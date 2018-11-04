from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from mototaxi.apps.conductores import views

urlpatterns = [
    path('conductores', views.ConductorList.as_view()),
    path('conductores/<int:pk>', views.ConductorDetail.as_view()),
   # path('moto/', views.MotoList.as_view()),
   # path('moto/<int:pk>', views.MotoDetail.as_view()),
]
urlpatterns=format_suffix_patterns(urlpatterns)