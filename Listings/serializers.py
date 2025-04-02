from rest_framework import serializers
from .models import Event, PropertyListing
from Users.serializers import UserSerializer
import datetime
# use Model Serializers when you want concise code and do automatically handle serialization of the classes
# Use Serializers when you want specific control 
class PropertyListingSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    class Meta:
        model = PropertyListing
        fields = '__all__'
        #exclude = ['potential_interest']

    def validate(self, data):
        if data['price'] <= 0:
            raise serializers.ValidationError("Price cannot be less than 0")
        if data['bedrooms'] <= 0:
            raise serializers.ValidationError("Bedrooms cannot be less than 0")
        return data


class EventSerializer(serializers.ModelSerializer):
    days_to_event = serializers.SerializerMethodField()
    class Meta:
        model = Event
        fields = '__all__'
    
    def get_days_to_event(self,event_model):
        return (event_model.date - datetime.date.today()).days
    # def event_time(self,)



# SerializerMethodField() --> This is serializer method that helps to add any custom logic to the serializer 
# items = serializers.SerializerMethodField()
# def get_items() --> get_<whatever_name_is_on_the_variable>:
# add any logic and it will show up on the response