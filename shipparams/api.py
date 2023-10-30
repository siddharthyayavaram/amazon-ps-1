from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from shipparams.models import Ship_params
from shipparams.serializers import Shipserializer

class Shiplist(APIView):
    def get(self, request):
        model = Ship_params.objects.all()
        serializer = Shipserializer(model, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Shipserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class Shipcost(APIView):
    def get(self, request, id):
        ship_params = Ship_params.objects.get(id=id)
        c= ship_params.cost  # Add the cost field to the response data
        return Response(c)
