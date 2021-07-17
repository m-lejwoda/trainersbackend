from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status
import stripe
stripe.api_key = "sk_test_9kDoV63WPpCjIGQqE95cfgql00L7UU3Wd8"


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


def stripe_session(request):
    stripe.checkout.Session.create(
        success_url="https://example.com/success",
        cancel_url="https://example.com/cancel",
        payment_method_types=["card"],
        line_items=[
            {
                "price": "price_H5ggYwtDq4fbrJ",
                "quantity": 2,
            },
        ],
        mode="payment",
    )
