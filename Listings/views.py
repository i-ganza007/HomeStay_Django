from .models import PropertyListing , Event
from .serializers import PropertyListingSerializer , EventSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def properties(request):
    properties = PropertyListing.objects.all()
    serializers = PropertyListingSerializer(properties,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def events(request):
    events = Event.objects.all()
    serializers = EventSerializer(events,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def property_view(request,pk:int):
    property = get_object_or_404(PropertyListing,pk=pk)
    serializer = PropertyListingSerializer(property)
    return Response(serializer.data)