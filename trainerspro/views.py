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
stripe.api_key = settings.STRIPE_API_KEY


@api_view(['GET'])
def index(self):
    return Response({"message": "Hello, world!"})


@api_view(['GET'])
def alltrainershours(request):
    if request.method == 'GET':
        events = Event.objects.filter(
            date=request.data['date'], trainer=request.data['user'])
        hours = TrainerHoursPerDay.objects.filter(user=request.data['user'])
        serializer = TrainerHoursPerDaySerializer(
            hours, many=True, context={'allevents': events})
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

def show_success_template(request):
    return render(request,'success.html')

def show_fail_template(request):
    return render(request,'fail.html')
