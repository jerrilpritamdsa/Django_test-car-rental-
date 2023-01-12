from django.shortcuts import render
from .models import Vehicle
from .serializers import VehicleSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView

class VehicleDetailView(APIView):
    
    
    def get(self, request):
        vehicle=  Vehicle.objects.all()
        serialzers  = VehicleSerializer(vehicle, many = True)
        return Response(serialzers.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializers = VehicleSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)
