from datetime import date
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_date(value):
        today = date.today()
        if value < today:
            raise serializers.ValidationError(_("Wrong date"))
        return value
def validate_training_numbers(training_numbers,events):
    if events >= training_numbers:
        raise serializers.ValidationError(_("Cant add another training probably you used whole plan"))
    return training_numbers