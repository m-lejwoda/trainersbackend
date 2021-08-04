from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import *
from .choices import WEEKDAYS
from django.utils.translation import ugettext_lazy as _
import time
from datetime import date,datetime

# class TrainerDaySerializer(serializers.Serializer):
#     first_name = serializers.CharField(source = "user.first_name")
#     last_name = serializers.CharField(source = "user.last_name")
#     from_hour = serializers.TimeField(required=True)
#     to_hour = serializers.TimeField(required=True)
#     user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
#     date = serializers.DateField()
#     # hours_list = serializers




class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields =  '__all__'
    
    def validate_date(self,value):
        today = date.today()
        if value < today:
            raise serializers.ValidationError(_("Wrong date"))
        return value
    def validate(self, attrs):
        hours = TrainerHoursPerDay.objects.filter(weekday=attrs['date'].weekday(),user=attrs['trainer'])
        events = Event.objects.filter(date=attrs['date'],trainer=attrs['trainer'])
        start_hour_split = attrs['start_hour'].strftime("%H:%M:%S").rsplit(':')[0]
        end_hour_split = attrs['end_hour'].strftime("%H:%M:%S").rsplit(':')[0]
        work_hours = [i for i in range(int(start_hour_split),int(end_hour_split)+1)]
        for event in events:
            if int(event.start_hour.strftime("%H:%M:%S").rsplit(':')[0]) in work_hours and int(event.end_hour.strftime("%H:%M:%S").rsplit(':')[0]) in work_hours:
                raise ValidationError({"error":_("Cant make reservation. Please refresh the page")})
        serializer = TrainerHoursPerDaySerializer(hours, many=True,context={'allevents': events})
        return super().validate(attrs)
    
class TrainerHoursPerDaySerializer(serializers.ModelSerializer):
    hours_list = serializers.SerializerMethodField()
    class Meta:
        model = TrainerHoursPerDay
        exclude = ['id','weekday','user']


    def get_date(self,obj):
        current_date = self.context.get("date")
        return current_date

    def get_weekday(self,obj):
        weekday = [obj.weekday,obj.get_weekday_display()]
        return weekday
        
    def get_hours_list(self,obj):
        str_from_hour_time = obj.from_hour.strftime("%H:%M:%S")
        str_to_hour_time = obj.to_hour.strftime("%H:%M:%S")
        list_from_hour_time = str_from_hour_time.rsplit(':')
        list_to_hour_time = str_to_hour_time.rsplit(':')
        hours_list = []
        events = self.context.get("events")
        for i in range(int(list_from_hour_time[0]),int(list_to_hour_time[0])):
            if i<10:
                first_value = "0" + str(i)
            else:
                first_value = str(i)
            if i+1<10:
                second_value = "0" + str(i+1)
            else:
                second_value = str(i+1)
            hours_list.append([first_value + ":" + list_from_hour_time[1]+ ":" + list_from_hour_time[2],second_value + ":" + list_to_hour_time[1]+ ":" + list_to_hour_time[2],True])
        print(hours_list)
        self.check_if_event(hours_list,events)
        return hours_list
    
    def check_if_event(self,hours,events):
        temp =None
        for hour in hours:
            start_hour_split = hour[0].rsplit(':')
            end_hour_split = hour[1].rsplit(':')
            for event in events:
                start_hour = getattr(event,'start_hour').strftime("%H:%M:%S").rsplit(':')
                end_hour = getattr(event,'end_hour').strftime("%H:%M:%S").rsplit(':')
                if start_hour_split[0] == start_hour[0]:
                    temp = start_hour_split[0]
                    hour[2] = False
                if temp != None:
                    hour[2] = False
                if end_hour_split[0] == end_hour[0]:
                    temp = None
                    if hour[2] != False:
                        hour[2] = False
    


class TrainerDaySerializer(serializers.Serializer):
    date = serializers.DateField()
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    first_name = serializers.CharField(source = "user.first_name")
    last_name = serializers.CharField(source = "user.last_name")
    weekday = serializers.SerializerMethodField()
    trainershour = TrainerHoursPerDaySerializer(many=True)
    def get_weekday(self,obj):
        return obj['date'].weekday()
    
    
class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields =  '__all__'
