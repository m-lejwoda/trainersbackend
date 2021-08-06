from celery import app, shared_task
from .models import Plan
from datetime import datetime,date

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
