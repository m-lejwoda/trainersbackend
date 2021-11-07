from celery import app, shared_task
from .models import Plan
from datetime import datetime,date
from django.core.mail import send_mail
from django.template.loader import render_to_string

@shared_task
def add(x, y):
    return x + y

@shared_task
def mul(x, y):
    return x * y

@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def checkplans():
    plans = Plan.plans.uncompleted()
    today = date.today()
    time=datetime.now().time()
    complete = False
    for plan in plans:
        if len(plan.events.all()) >= plan.package_num:
            for event in plan.events.all():
                if event.date < today:
                    if time >= event.end_hour:
                        pass
                elif event.date == today:
                    pass
    return "ses"

@shared_task
def send_create_plan_mail(data):
    print("send_create_plan_mail")
    print(data)
    context= {
        'id': data['id'],
        'client_name': data['client_name'],
        'client_email': data['client_email'],
        'client_phone': data['client_phone'],
        'package_name': data['package_name'],
        'trainer_name': data['trainer_name'],
        'trainer_phone': data['trainer_phone'],
        'last_name': data['last_name'],
        'event' : data['events'][0],
        'url' : "http://127.0.0.1:8000/api/"

    }
    html_message = render_to_string('email_first_plan.html',context=context)
    send_mail(
    'Utworzono pakiet',
    'Here is the message.',
    'from@example.com',
    [data['client_email']],
    html_message= html_message,
    fail_silently=False,
)

@shared_task
def send_mail_with_add_event_to_plan(data,eventdata,left_trainings):
    print(left_trainings)
    context= {
        'id': data['id'],
        'client_name': data['client_name'],
        'client_email': data['client_email'],
        'client_phone': data['client_phone'],
        'trainer_name': data['trainer_name'],
        'trainer_phone': data['trainer_phone'],
        'trainer': data['trainer'],
        'last_name': data['last_name'],
        'event' : eventdata,
        'url' : "http://127.0.0.1:8000/api/",
        'left_trainings': left_trainings
    }
    html_message = render_to_string('email_add_event_to_plan.html',context=context)
    send_mail(
    'Trening dodany do pakietu',
    'Here is the message.',
    'from@example.com',
    [data['client_email']],
    html_message= html_message,
    fail_silently=False,
)