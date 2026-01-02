from rest_framework import serializers
from .models import *

class BussSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buss
        fields = '__all__'
        
        
class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
        
        
class ReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = ['id', 'trip', 'seat_number']
        
    def validate_seat_number(self, value):
        trip_id = self.initial_data.get('trip')
        if not trip_id:
            raise serializers.ValidationError("الرحلة مكيناش")

        try:
            trip = Trip.objects.get(id=trip_id)
        except Trip.DoesNotExist:
            raise serializers.ValidationError("الرحلة غير موجودة")

        bus = trip.buss
        if value < 1 or value > bus.seats:
            raise serializers.ValidationError(f"المقعد {value} غير موجود في هذا الباص، عدد المقاعد: {bus.seats}")

        if Reservations.objects.filter(trip=trip, seat_number=value).exists():
            raise serializers.ValidationError("هذا المقعد محجوز بالفعل")

        return value