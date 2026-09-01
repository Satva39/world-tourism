from django.urls import path

from .views import flight_search

urlpatterns = [
    path("flights/", flight_search, name="flight-search"),
]
