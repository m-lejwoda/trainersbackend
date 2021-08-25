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
    path('add_consultation',add_private_consultation,name='add_private_consultation'),
    path('add_plan_with_event',add_plan_with_event,name='add_plan_with_event'),
    path('add_event_to_plan',add_event_to_plan,name='add_event_to_plan'),
    path('get_trainers',get_trainers,name='get_trainers'),
    path('get_packages',get_packages,name='get_packages'),
    path('get_trainers_with_image',get_trainers_with_image,name='get_trainers_with_image'),
    path('get_three_transformations',get_three_transformations,name='get_three_transformations'),
    path('get_all_transformations',GetAllTransformations.as_view(),name='get_all_transformations')
    
    # path('trainerhourswithdate',trainerhourswithdate,name='trainerhourswithdate')
]