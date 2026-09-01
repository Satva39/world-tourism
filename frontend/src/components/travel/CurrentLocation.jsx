import { useState } from "react";

function CurrentLocation({ onLocation, disabled = false }) {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    function getLocation() {
        if (!navigator.geolocation) {
            setError("Location services are not supported by this browser.");
            return;
        }

        setLoading(true);
        setError("");

        navigator.geolocation.getCurrentPosition(
            (position) => {
                const { latitude, longitude, accuracy } = position.coords;

                onLocation({
                    latitude,
                    longitude,
                    accuracy,
                });

                setLoading(false);
            },
            (locationError) => {
                setLoading(false);

                switch (locationError.code) {
                    case locationError.PERMISSION_DENIED:
                        setError(
                            "Location permission was denied. Please allow location access and try again."
                        );
                        break;

                    case locationError.POSITION_UNAVAILABLE:
                        setError(
                            "Your current location could not be determined."
                        );
                        break;

                    case locationError.TIMEOUT:
                        setError(
                            "Location request timed out. Please try again."
                        );
                        break;

                    default:
                        setError(
                            "Could not determine your current location."
                        );
                }
            },
            {
                enableHighAccuracy: true,
                timeout: 10000,
                maximumAge: 300000,
            }
        );
    }

    return (
        <div className="current-location">
            <button
                type="button"
                className="current-location__button"
                onClick={getLocation}
                disabled={disabled || loading}
            >
                <span className="current-location__icon">
                    {loading ? "…" : "⌖"}
                </span>

                <span>
                    {loading
                        ? "Detecting location..."
                        : "Use my current location"}
                </span>
            </button>

            {error && (
                <p
                    className="current-location__error"
                    role="alert"
                >
                    {error}
                </p>
            )}
        </div>
    );
}

export default CurrentLocation;