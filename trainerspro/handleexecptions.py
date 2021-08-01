from datetime import date
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


def validate_date(value):
        today = date.today()
        if value < today:
            raise serializers.ValidationError("Wrong date")
        return value
    