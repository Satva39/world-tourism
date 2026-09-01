import json

from travel.services.duffel import DuffelFlightProvider


provider = DuffelFlightProvider()

airports = provider.find_nearby_airports(
    latitude=19.0760,
    longitude=72.8777,
)

print(json.dumps(airports[:5], indent=2))