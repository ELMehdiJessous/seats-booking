from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Buss(models.Model):
    number = models.CharField(max_length=50)
    seats = models.IntegerField()
     
    def __str__(self):
        return self.number
    
class Trip(models.Model):
    buss = models.ForeignKey(Buss, on_delete=models.CASCADE)
    from_city = models.CharField(max_length=100)
    to_city = models.CharField(max_length=100)
    deprature_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
       
class Reservations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip,on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    
    class Meta:
        unique_together = ['trip','seat_number']