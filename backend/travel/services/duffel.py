import requests

from app.core.config import settings


class DuffelFlightProvider:
    """Duffel flight-search and Duffel Links adapter."""

    def __init__(self):
        self.base_url = settings.duffel_base_url.rstrip("/")
        self.api_key = settings.duffel_api_key

        self.success_url = settings.duffel_success_url
        self.failure_url = settings.duffel_failure_url
        self.abandonment_url = settings.duffel_abandonment_url

    def _headers(self):
        if not self.api_key:
            raise RuntimeError("Duffel API key is not configured.")

        return {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Duffel-Version": "v2",
        }

    def search(
        self,
        origin,
        destination,
        departure_date,
        adults=1,
    ):
        response = requests.post(
            f"{self.base_url}/air/offer_requests",
            headers=self._headers(),
            json={
                "data": {
                    "slices": [
                        {
                            "origin": origin,
                            "destination": destination,
                            "departure_date": departure_date,
                        }
                    ],
                    "passengers": [{"type": "adult"} for _ in range(adults)],
                    "cabin_class": "economy",
                }
            },
            timeout=30,
        )

        response.raise_for_status()
        return response.json()

    def create_booking_link(self, offer_id: str | None = None):
        """
        Create a Duffel Links session.

        Duffel Links creates a Duffel-hosted search/booking experience.
        The offer_id is used only as our session reference.
        """

        url = f"{self.base_url}/links/sessions"

        payload = {
            "data": {
                "reference": offer_id or "world-tourism-user",
                "success_url": self.success_url,
                "failure_url": self.failure_url,
                "abandonment_url": self.abandonment_url,
                "flights": {
                    "enabled": "true",
                },
                "stays": {
                    "enabled": "false",
                },
            }
        }

        response = requests.post(
            url,
            headers=self._headers(),
            json=payload,
            timeout=30,
        )

        if not response.ok:
            raise RuntimeError(
                f"Duffel Links error {response.status_code}: " f"{response.text}"
            )

        result = response.json()
        data = result.get("data") or {}

        # Duffel Links returns the hosted URL in data.url.
        booking_url = data.get("url")

        if not booking_url:
            raise RuntimeError(
                f"Duffel Links response did not contain data.url: " f"{result}"
            )

        return {
            "url": booking_url,
            "reference": data.get("reference"),
        }

    def find_nearby_airports(
        self,
        latitude,
        longitude,
        radius=100000,
    ):
        response = requests.get(
            f"{self.base_url}/places/suggestions",
            headers=self._headers(),
            params={
                "lat": latitude,
                "lng": longitude,
                "rad": radius,
            },
            timeout=20,
        )

        response.raise_for_status()

        data = response.json().get("data", [])

        return [
            place
            for place in data
            if (place.get("type") == "airport" and place.get("iata_code"))
        ]
