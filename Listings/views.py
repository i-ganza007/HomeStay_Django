from .models import PropertyListing
from .serializers import PropertyListingSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def properties(request):
    properties = PropertyListing.objects.all()
    serializers = PropertyListingSerializer(properties,many=True)
    return Response(serializers.data)