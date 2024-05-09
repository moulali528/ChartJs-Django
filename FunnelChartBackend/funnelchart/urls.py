# from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.funnelChartView, name='funnel-chart-view'),
    path('react-view', ReactView.as_view(), name='react-view')
]