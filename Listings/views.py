from multiprocessing import context
from .models import PropertyListing , Event
from django.shortcuts import render
from .serializers import PropertyListingSerializer , EventSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

from django.shortcuts import get_object_or_404

# @api_view(['GET'])
# def properties(request):
#     properties = PropertyListing.objects.all()
#     serializers = PropertyListingSerializer(properties,many=True)
#     return Response(serializers.data)

class PropertyAPIView(generics.ListAPIView):
    queryset = PropertyListing.objects.all()
    serializer_class = PropertyListingSerializer

# @api_view(['GET'])
# def events(request):
#     events = Event.objects.all()
#     serializers = EventSerializer(events,many=True)
#     return Response(serializers.data)
class EventAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# @api_view(['GET'])
# def property_view(request,pk:int):
#     property = get_object_or_404(PropertyListing,pk=pk)
#     serializer = PropertyListingSerializer(property)
#     return Response(serializer.data)
class IndPropertyView(generics.RetrieveAPIView):
    queryset = PropertyListing.objects.all()
    serializer_class = PropertyListingSerializer
    lookup_field = 'id'

def home(request):
    return render(request,'Listings/home.html')

def property(request):
    data = PropertyListing.objects.all()
    return render(request,'Listings/properties.html',{'context':data})