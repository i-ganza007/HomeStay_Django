from rest_framework import serializers
from .models import Event, PropertyListing


class PropertyListingSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ('description', 'event_name')
