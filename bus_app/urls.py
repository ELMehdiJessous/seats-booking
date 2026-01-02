from django.urls import path
from . import views

urlpatterns = [
    path('trips/',views.trips_list),
    path('reserve/',views.reserve_seat),
]