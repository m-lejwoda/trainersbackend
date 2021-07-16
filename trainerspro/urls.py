from .views import *
from django.urls import path


urlpatterns = [
    path('example', index, name='example'),
    path('alltrainershours',alltrainershours,name='alltrainershours'),
    # path('trainerhourswithdate',trainerhourswithdate,name='trainerhourswithdate')
]