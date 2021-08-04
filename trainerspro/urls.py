from .views import *
from django.urls import path,include


urlpatterns = [
    path('example', index, name='example'),
    path('alltrainershours',alltrainershours,name='alltrainershours'),
    path('showsuccess',show_success_template,name='show_success_template'),
    path('showfail',show_fail_template,name='show_fail_template'),
    path('stripe_session',stripe_session,name='stripe_session'),
    path('add_post',add_post,name='add_post'),
    path('add_event',add_event,name='add_event'),
    path('training_by_day',trainingbyday,name='training_by_day'),
    path('add_event_by_trainer',trainer_add_event,name='trainer_add_event'),
    path('mainpage',trainer_mainpage,name="trainer_mainpage"),
    path('add_consultation',add_private_consultation,name='add_private_consultation')
    
    # path('trainerhourswithdate',trainerhourswithdate,name='trainerhourswithdate')
]