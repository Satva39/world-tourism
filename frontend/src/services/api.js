const API_BASE_URL =
    import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000/api";

async function apiRequest(endpoint) {
    const response = await fetch(`${API_BASE_URL}${endpoint}`);

    if (!response.ok) {
        throw new Error(`API request failed: ${response.status}`);
    }

    return response.json();
}

export function getCountries() {
    return apiRequest("/countries/");
}

export function getCountry(countryId) {
    return apiRequest(`/countries/${countryId}`);
}

export function getCountryRegions(countryId) {
    return apiRequest(`/countries/${countryId}/regions`);
}

export async function searchFlights({
    originLatitude,
    originLongitude,
    destinationLatitude,
    destinationLongitude,
    departureDate,
    adults = 1,
}) {
    const params = new URLSearchParams({
        origin_latitude: originLatitude,
        origin_longitude: originLongitude,
        destination_latitude: destinationLatitude,
        destination_longitude: destinationLongitude,
        departure_date: departureDate,
        adults,
    });

    const response = await fetch(
        `${API_BASE_URL}/travel/flights?${params.toString()}`
    );

    const data = await response.json();

    if (!response.ok) {
        throw new Error(
            data.detail || data.message || "Could not search flights."
        );
    }

    return data;
}