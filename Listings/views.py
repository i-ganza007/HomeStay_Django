from tempfile import template
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

class EventAPIView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = 'id'

# @api_view(['GET'])
# def property_view(request,pk:int):
#     property = get_object_or_404(PropertyListing,pk=pk)
#     serializer = PropertyListingSerializer(property)
#     return Response(serializer.data)
class IndPropertyView(generics.RetrieveAPIView):
    queryset = PropertyListing.objects.all()
    serializer_class = PropertyListingSerializer
    lookup_field = 'id'
# You can tie a serializer to a model instead of a queryset 
# You can also tie multiple types of requests either get or post , to a single endpoint : To do this there are some more generic api views (ListAPICreateView)
# Check out classy django rest framework for everything about CBV 
# class CreateView(generics.CreateAPIView):
#     queryset = ----
#     serializer = ----
#     def create(self,request,*args,**kwargs):
#         return super().create(---) --> This called the inherited class by calling super() and then calling the create() method w
def home(request):
    return render(request,'Listings/home.html')

def property(request):
    data = PropertyListing.objects.all()
    return render(request,'Listings/properties.html',{'context':data})
