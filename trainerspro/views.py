from trainersdjango.settings import STRIPE_API_KEY
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status
from django.shortcuts import render 
import stripe
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from .forms import PostForm,TrainerEventForm
from datetime import datetime
from .handleexceptions import validate_date,validate_training_numbers
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .tasks import send_create_plan_mail


stripe.api_key = settings.STRIPE_API_KEY


def add_post(request):
    form = PostForm()
    context = {'form':form}
    return render(request,'add_post.html',context)

@api_view(['GET'])
def index(self):
    return Response({"message": "Hello, world!"})

@api_view(['POST'])
def add_event_to_plan(request):
    if request.method == 'POST':
        plan = Plan.objects.get(id = request.data['id'])
        validate_training_numbers(plan.training_numbers(),len(plan.events.all()))
        serializer = EventsSerializer(data=request.data)
        planserializer = PlanSerializer(plan)
        if serializer.is_valid():
            serializer.save()
            plan.events.add(serializer.data['id'])
            return Response(planserializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_trainers(request):
    if request.method == 'GET':
        customusers = CustomUser.objects.all()
        serializer = TrainerSerializer(customusers,many=True)
        return Response(serializer.data)


@api_view(['POST'])
def add_plan_with_event(request):
    if request.method == 'POST':
        serializer = PlanSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            send_create_plan_mail(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)
            
                
@api_view(['POST'])
def add_event(request):
    if request.method == 'POST':
        serializer = EventsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)

def trainer_add_event(request):
    form = TrainerEventForm(request.POST or None,initial={'trainer': request.user})
    if form.is_valid():
        form.save()
        form=TrainerEventForm()
    context = {'form': form}
    return render(request,'trainer_add_event.html',context)

def trainer_mainpage(request):
    return render(request,'trainer_page.html')

def add_private_consultation(request):
    form = TrainerEventForm(request.POST or None,initial={'trainer': request.user})
    if form.is_valid():
        form.save()
        form=TrainerEventForm()
    context = {'form': form}
    return render(request,'add_private_consultation.html',context)
@api_view(['GET'])
def alltrainershours(request):
    if request.method == 'GET':
        date = datetime.strptime(request.data['date'],"%Y-%m-%d").date()
        events = Event.objects.filter(
            date=request.data['date'], trainer=request.data['user'])
        hours = TrainerHoursPerDay.objects.filter(user=request.data['user'],weekday=date.weekday())
        serializer = TrainerHoursPerDaySerializer(hours, many=True, context={'allevents': events,'date':date})
        return Response(serializer.data)

# @api_view(['GET'])
# def getactiveplans()

@api_view(['GET'])
def trainingbyday(request):
    if request.method == 'GET':
        current_date = datetime.strptime(request.data['date'],"%Y-%m-%d").date()
        user = CustomUser.objects.get(pk=request.data['user'])
        hours = TrainerHoursPerDay.objects.filter(user=request.data['user'],weekday=current_date.weekday())  
        events = Event.objects.filter(trainer=request.data['user'],date=current_date)
        data = {"date": current_date,"trainershour":hours,"user":user}
        serializer = TrainerDaySerializer(data,context={"events": events})
        return Response(serializer.data)

@api_view(['POST'])
def stripe_session(request):
    stripe_session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/api/showsuccess",
        cancel_url="http://127.0.0.1:8000/api/failsuccess",
        payment_method_types=["card","p24"],
        line_items=[
            {
                "price": "price_1JEKReKoR4wmJw304pg4VS2l",
                "quantity": 1,
            },
        ],
        mode="payment",
    )
    return Response(stripe_session)

@cache_page(60 * 15)
def show_success_template(request):
    return render(request,'success.html')

def show_fail_template(request):
    return render(request,'fail.html')
