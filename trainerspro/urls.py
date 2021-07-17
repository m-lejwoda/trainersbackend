from .views import *
from django.urls import path


urlpatterns = [
    path('example', index, name='example'),
    path('alltrainershours',alltrainershours,name='alltrainershours'),
    path('showsuccess',show_success_template,name='show_success_template'),
    path('showfail',show_fail_template,name='show_fail_template'),
    path('stripe_session',stripe_session,name='stripe_session')
    # path('trainerhourswithdate',trainerhourswithdate,name='trainerhourswithdate')
]