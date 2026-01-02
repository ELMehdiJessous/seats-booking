from rest_framework.decorators import api_view, permission_classes ,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.contrib.auth.models import User

# 👀 User يشوف الرحلات
@api_view(['GET'])
def trips_list(request):
    trips = Trip.objects.all()
    serializer = TripSerializer(trips, many=True)
    return Response(serializer.data)

# 🎟️ User يحجز (Token Required)
@api_view(['POST'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def reserve_seat(request):
    serializer = ReservationsSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=400)