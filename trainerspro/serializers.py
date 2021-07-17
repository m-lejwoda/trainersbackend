from rest_framework import serializers
from .models import *
from .choices import WEEKDAYS
import time


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields =  '__all__'


class TrainerHoursPerDaySerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source = "user.first_name")
    last_name = serializers.CharField(source = "user.last_name")
    weekday = serializers.SerializerMethodField()
    hours_list = serializers.SerializerMethodField()
    events = serializers.SerializerMethodField()
    date = serializers.DateTimeField(default=None)
    class Meta:
        model = TrainerHoursPerDay
        fields =  '__all__'

    def get_weekday(self,obj):
        return obj.get_weekday_display()
        
    def get_hours_list(self,obj):
        str_from_hour_time = obj.from_hour.strftime("%H:%M:%S")
        str_to_hour_time = obj.to_hour.strftime("%H:%M:%S")
        list_from_hour_time = str_from_hour_time.rsplit(':')
        list_to_hour_time = str_to_hour_time.rsplit(':')
        hours_list = []
        events = self.context.get("allevents")
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
        self.check_if_event(hours_list,events)
        
        return hours_list
    def get_events(self,obj):
        objects = Event.objects.all()
        event = EventsSerializer(objects,many=True)
        return event.data
    
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


    
    
