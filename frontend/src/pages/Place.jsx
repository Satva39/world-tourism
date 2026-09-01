import { useEffect, useMemo, useState } from "react";
import { Link, useParams } from "react-router-dom";
import CurrentLocation from "../components/travel/CurrentLocation";
import API_BASE_URL from "../config/api";
import {
    MapContainer,
    Marker,
    Popup,
    TileLayer,
} from "react-leaflet";
import "leaflet/dist/leaflet.css";

function Place() {

    // const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

    const getImageUrl = (image) => {
        if (!image) return null;

        const imageUrl =
            image.image_url ||
            image.url ||
            image.image ||
            null;

        if (!imageUrl) return null;

        // Absolute URL
        if (imageUrl.startsWith("http://") || imageUrl.startsWith("https://")) {
            return imageUrl;
        }

        // Backend-served image
        if (imageUrl.startsWith("/")) {
            return `${API_BASE_URL}${imageUrl}`;
        }

        return imageUrl;
    };

    const { countryId, stateId, placeId } = useParams();

    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");
    const [copied, setCopied] = useState(false);
    const [imageErrors, setImageErrors] = useState({});
    const [userLocation, setUserLocation] = useState(null);
    const [travelOptions, setTravelOptions] = useState(null);
    const [travelLoading, setTravelLoading] = useState(false);
    const [travelError, setTravelError] = useState("");

    useEffect(() => {
        let cancelled = false;

        async function fetchPlaceDetails() {
            try {
                setLoading(true);
                setError("");

                const response = await fetch(
                    `${import.meta.env.VITE_API_BASE_URL}/place-details/${placeId}`
                );
                if (!response.ok) {
                    throw new Error(
                        `Could not load place details (${response.status})`
                    );
                }

                const result = await response.json();

                if (!cancelled) {
                    setData(result);
                }
            } catch (err) {
                if (!cancelled) {
                    setError(
                        err instanceof Error
                            ? err.message
                            : "Could not load place details."
                    );
                }
            } finally {
                if (!cancelled) {
                    setLoading(false);
                }
            }
        }

        fetchPlaceDetails();

        return () => {
            cancelled = true;
        };
    }, [placeId]);

    const images = useMemo(
        () =>
            (data?.images || [])
                .filter((image) => !imageErrors[image.id])
                .sort((a, b) => {
                    if (a.is_cover && !b.is_cover) return -1;
                    if (!a.is_cover && b.is_cover) return 1;
                    return (a.sort_order ?? 0) - (b.sort_order ?? 0);
                }),
        [data?.images, imageErrors]
    );

    const coverImage =
        data?.images?.find((image) => image.is_cover) ||
        data?.images?.[0];

    const coverImageUrl = getImageUrl(coverImage);

    const mapUrl =
        data?.place?.latitude != null && data?.place?.longitude != null
            ? `https://www.google.com/maps/search/?api=1&query=${data.place.latitude},${data.place.longitude}`
            : null;

    const coordinates =
        data?.place?.latitude != null && data?.place?.longitude != null
            ? `${Number(data.place.latitude).toFixed(4)}, ${Number(
                data.place.longitude
            ).toFixed(4)}`
            : null;

    async function copyCoordinates() {
        if (!coordinates || !navigator.clipboard) return;

        try {
            await navigator.clipboard.writeText(coordinates);
            setCopied(true);
            window.setTimeout(() => setCopied(false), 1800);
        } catch {
            setCopied(false);
        }
    }

    function handleImageError(imageId) {
        setImageErrors((current) => ({
            ...current,
            [imageId]: true,
        }));
    }

    const destinationLocation = useMemo(() => {
        const latitude = Number(data?.place?.latitude);
        const longitude = Number(data?.place?.longitude);

        if (
            !Number.isFinite(latitude) ||
            !Number.isFinite(longitude)
        ) {
            return null;
        }

        return {
            latitude,
            longitude,
        };
    }, [data]);

    const travelRoute = useMemo(() => {
        if (!userLocation || !destinationLocation) {
            return null;
        }

        return {
            origin: {
                latitude: userLocation.latitude,
                longitude: userLocation.longitude,
            },
            destination: {
                latitude: destinationLocation.latitude,
                longitude: destinationLocation.longitude,
            },
        };
    }, [userLocation, destinationLocation]);

    async function handleFlightBooking(offerId) {
        try {
            const response = await fetch(
                `${API_BASE_URL}/api/travel/flights/${offerId}/booking-link`,
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                }
            );

            const result = await response.json();

            if (!response.ok) {
                throw new Error(
                    result.detail || "Could not create booking link."
                );
            }

            window.open(result.url, "_blank", "noopener,noreferrer");
        } catch (err) {
            setTravelError(
                err instanceof Error
                    ? err.message
                    : "Could not open booking."
            );
        }
    }

    async function searchTravelOptions() {
        if (!travelRoute) return;

        try {
            setTravelLoading(true);
            setTravelError("");
            setTravelOptions(null);

            const tomorrow = new Date();
            tomorrow.setDate(tomorrow.getDate() + 1);

            const departureDate = tomorrow.toISOString().split("T")[0];

            const params = new URLSearchParams({
                origin_latitude: String(travelRoute.origin.latitude),
                origin_longitude: String(travelRoute.origin.longitude),
                destination_latitude: String(
                    travelRoute.destination.latitude
                ),
                destination_longitude: String(
                    travelRoute.destination.longitude
                ),
                departure_date: departureDate,
                adults: "1",
            });

            const response = await fetch(
                `${API_BASE_URL}/api/travel/flights?${params.toString()}`
            );

            const result = await response.json();

            if (!response.ok) {
                throw new Error(
                    result.detail ||
                    result.message ||
                    "Could not find flights."
                );
            }

            setTravelOptions(result);
        } catch (err) {
            setTravelError(
                err instanceof Error
                    ? err.message
                    : "Could not find flights."
            );
        } finally {
            setTravelLoading(false);
        }
    }

    if (loading) {
        return (
            <main className="place-page">
                <div className="place-loading">
                    <div className="place-loading__spinner" />
                    <span>Exploring destination...</span>
                </div>
            </main>
        );
    }

    if (error || !data?.place) {
        return (
            <main className="place-page">
                <div className="place-container">
                    <div className="error-card">
                        <span className="section-label">TRAVEL ERROR</span>
                        <h1>We couldn't load this destination</h1>
                        <p>
                            {error ||
                                "The requested destination could not be found."}
                        </p>

                        <Link
                            to={`/country/${countryId}/state/${stateId}`}
                            className="back-link"
                        >
                            ← Back to State
                        </Link>
                    </div>
                </div>
            </main>
        );
    }

    const { place, details } = data;

    return (
        <main className="place-page">
            <div className="place-container">
                {/* Breadcrumb */}
                <nav className="breadcrumb" aria-label="Breadcrumb">
                    <Link to="/">Home</Link>
                    <span>/</span>
                    <Link to={`/country/${countryId}`}>Country</Link>
                    <span>/</span>
                    <Link
                        to={`/country/${countryId}/state/${stateId}`}
                    >
                        State
                    </Link>
                    <span>/</span>
                    <strong>{place.name}</strong>
                </nav>

                {/* Hero */}
                <section className="place-hero">
                    {coverImageUrl ? (
                        <img
                            src={coverImageUrl}
                            alt={coverImage?.alt_text || place.name}
                            className="place-cover-image"
                        />
                    ) : (
                        <div className="place-cover-placeholder">
                            <span>{place.name}</span>
                        </div>
                    )}

                    <div className="place-hero__overlay" />
                    <div className="place-hero__glow" />

                    <div className="place-hero__content">
                        <span className="section-label">DESTINATION</span>

                        <h1>{place.name}</h1>

                        {place.short_description && (
                            <p>{place.short_description}</p>
                        )}

                        <div className="place-hero__actions">
                            {mapUrl && (
                                <a
                                    href={mapUrl}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className="hero-action"
                                >
                                    <span>↗</span>
                                    Open in Maps
                                </a>
                            )}

                            {coordinates && (
                                <button
                                    type="button"
                                    className="hero-action hero-action--ghost"
                                    onClick={copyCoordinates}
                                >
                                    <span>{copied ? "✓" : "⌖"}</span>
                                    {copied ? "Coordinates Copied" : "Copy Coordinates"}
                                </button>
                            )}
                        </div>
                    </div>

                    <div className="place-hero__meta">
                        <span>Explore</span>
                        <strong>{place.name}</strong>
                    </div>
                </section>

                {/* Gallery */}
                {images.length > 0 && (
                    <section className="place-gallery">
                        <div className="section-heading">
                            <div>
                                <span className="section-label">GALLERY</span>
                                <h2>Explore {place.name}</h2>
                            </div>

                            <span className="gallery-count">
                                {images.length}{" "}
                                {images.length === 1 ? "photo" : "photos"}
                            </span>
                        </div>

                        <div className="place-gallery-grid">
                            {images.map((image) => {
                                const imageUrl = getImageUrl(image);

                                if (!imageUrl) return null;

                                return (
                                    <div
                                        key={image.id}
                                        className="place-gallery-item"
                                    >
                                        <img
                                            src={imageUrl}
                                            alt={image.alt_text || place.name}
                                            loading="lazy"
                                            onError={() =>
                                                handleImageError(image.id)
                                            }
                                        />

                                        {image.is_cover && (
                                            <span className="place-gallery-badge">
                                                Featured
                                            </span>
                                        )}
                                    </div>
                                );
                            })}
                        </div>
                    </section>
                )}

                {/* Quick facts */}
                <section className="place-content-grid">
                    <article className="place-card place-card--about">
                        <div className="place-card__topline">
                            <span className="section-label">DISCOVER</span>
                            <span className="place-card__icon">✦</span>
                        </div>

                        <h2>About {place.name}</h2>

                        <p>
                            {place.description ||
                                place.short_description ||
                                "Information about this destination will be available soon."}
                        </p>
                    </article>

                    <article className="place-card place-card--location">
                        <div className="place-card__topline">
                            <span className="section-label">LOCATION</span>
                            <span className="place-card__icon">⌖</span>
                        </div>

                        <h2>Where it is</h2>

                        <div className="info-list">
                            <div className="info-row">
                                <span>Latitude</span>
                                <strong>
                                    {place.latitude ?? "N/A"}
                                </strong>
                            </div>

                            <div className="info-row">
                                <span>Longitude</span>
                                <strong>
                                    {place.longitude ?? "N/A"}
                                </strong>
                            </div>

                            {coordinates && (
                                <div className="info-row">
                                    <span>Coordinates</span>
                                    <strong>{coordinates}</strong>
                                </div>
                            )}
                        </div>
                    </article>
                </section>

                {/* Map */}
                {place.latitude != null && place.longitude != null && (
                    <section className="place-map-section">
                        <div className="section-heading">
                            <div>
                                <span className="section-label">MAP</span>
                                <h2>Find your way to {place.name}</h2>
                            </div>

                            {mapUrl && (
                                <a
                                    href={mapUrl}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className="section-link"
                                >
                                    Open full map ↗
                                </a>
                            )}
                        </div>

                        <div className="place-map">
                            <MapContainer
                                center={[place.latitude, place.longitude]}
                                zoom={12}
                                scrollWheelZoom={false}
                                style={{ height: "420px", width: "100%" }}
                            >
                                <TileLayer
                                    attribution="&copy; OpenStreetMap contributors"
                                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                                />

                                <Marker
                                    position={[
                                        place.latitude,
                                        place.longitude,
                                    ]}
                                >
                                    <Popup>
                                        <strong>{place.name}</strong>
                                        <br />
                                        {coordinates}
                                    </Popup>
                                </Marker>
                            </MapContainer>
                        </div>
                    </section>
                )}

                {/* Travel information */}
                <section className="place-details-section">
                    <div className="section-heading">
                        <div>
                            <span className="section-label">
                                PLAN YOUR VISIT
                            </span>
                            <h2>Travel Information</h2>
                        </div>
                    </div>

                    <div className="details-grid">
                        <article className="detail-card">
                            <span className="detail-card__label">
                                ENTRY FEE
                            </span>
                            <span className="detail-card__icon">₹</span>
                            <h3>
                                {details?.entry_fee || "Not available"}
                            </h3>
                        </article>

                        <article className="detail-card">
                            <span className="detail-card__label">
                                OPENING HOURS
                            </span>
                            <span className="detail-card__icon">◷</span>
                            <h3>
                                {details?.opening_hours ||
                                    "Not available"}
                            </h3>
                        </article>

                        <article className="detail-card">
                            <span className="detail-card__label">
                                BEST TIME
                            </span>
                            <span className="detail-card__icon">☀</span>
                            <h3>
                                {details?.best_time || "Not available"}
                            </h3>
                        </article>

                        <article className="detail-card">
                            <span className="detail-card__label">
                                RECOMMENDED DURATION
                            </span>
                            <span className="detail-card__icon">⌛</span>
                            <h3>
                                {details?.duration || "Not available"}
                            </h3>
                        </article>
                    </div>
                </section>

                {/* Travel assistance */}
                <section className="travel-assistance-section">
                    <div className="section-heading">
                        <div>
                            <span className="section-label">
                                PLAN YOUR JOURNEY
                            </span>

                            <h2>
                                How do you want to reach {place.name}?
                            </h2>
                        </div>

                        <p>
                            Find travel options from your current location.
                        </p>
                    </div>

                    <div className="travel-location-card">
                        {!userLocation && (
                            <>
                                <div className="travel-location-card__content">
                                    <span className="travel-location-card__label">
                                        STARTING LOCATION
                                    </span>

                                    <h3>Where are you starting from?</h3>

                                    <p>
                                        Allow location access so we can find available travel
                                        options from your location.
                                    </p>
                                </div>

                                <CurrentLocation
                                    onLocation={setUserLocation}
                                />
                            </>
                        )}

                        {userLocation && (
                            <div className="travel-location-card__detected">
                                <span className="travel-location-card__detected-dot" />
                                <strong>Starting location detected</strong>
                            </div>
                        )}

                        {travelRoute && (
                            <button
                                type="button"
                                className="travel-search-button"
                                onClick={searchTravelOptions}
                                disabled={travelLoading}
                            >
                                {travelLoading
                                    ? "Finding travel options..."
                                    : "Find Travel Options →"}
                            </button>
                        )}

                        {travelError && (
                            <p className="travel-search-error">
                                {travelError}
                            </p>
                        )}

                        {travelOptions && (
                            <div className="travel-search-result">
                                {!travelOptions.success ? (
                                    <p>{travelOptions.message}</p>
                                ) : (
                                    <>
                                        <h3>Available Flights</h3>

                                        {travelOptions.origin?.airport && (
                                            <p>
                                                From{" "}
                                                <strong>
                                                    {travelOptions.origin.airport.iata_code}
                                                </strong>{" "}
                                                — {travelOptions.origin.airport.name}
                                            </p>
                                        )}

                                        {travelOptions.destination?.airport && (
                                            <p>
                                                To{" "}
                                                <strong>
                                                    {travelOptions.destination.airport.iata_code}
                                                </strong>{" "}
                                                — {travelOptions.destination.airport.name}
                                            </p>
                                        )}

                                        <div className="travel-options-grid">
                                            {(travelOptions.results?.data?.offers || []).map(
                                                (offer) => {
                                                    const slice = offer.slices?.[0];
                                                    const segment = slice?.segments?.[0];

                                                    const airline =
                                                        segment?.marketing_carrier?.name ||
                                                        segment?.operating_carrier?.name ||
                                                        "Airline";

                                                    const departure =
                                                        segment?.departing_at
                                                            ? new Date(
                                                                segment.departing_at
                                                            ).toLocaleTimeString([], {
                                                                hour: "2-digit",
                                                                minute: "2-digit",
                                                            })
                                                            : "—";

                                                    const arrival =
                                                        segment?.arriving_at
                                                            ? new Date(
                                                                segment.arriving_at
                                                            ).toLocaleTimeString([], {
                                                                hour: "2-digit",
                                                                minute: "2-digit",
                                                            })
                                                            : "—";

                                                    return (
                                                        <button
                                                            key={offer.id}
                                                            type="button"
                                                            className="travel-option-card"
                                                            onClick={() => handleFlightBooking(offer.id)}
                                                        >
                                                            <span className="travel-option-type">
                                                                FLIGHT
                                                            </span>

                                                            <h4>{airline}</h4>

                                                            <p>
                                                                {segment?.origin?.iata_code ||
                                                                    "—"}{" "}
                                                                →{" "}
                                                                {segment?.destination?.iata_code ||
                                                                    "—"}
                                                            </p>

                                                            <p>
                                                                {departure} → {arrival}
                                                            </p>

                                                            <strong>
                                                                {offer.total_currency}{" "}
                                                                {offer.total_amount}
                                                            </strong>
                                                        </button>
                                                    );
                                                }
                                            )}
                                        </div>
                                    </>
                                )}
                            </div>
                        )}

                    </div>
                </section>

                {/* Getting there / facilities */}
                <div className="place-info-grid">
                    {details?.how_to_reach && (
                        <section className="place-info-section">
                            <article className="place-card">
                                <span className="section-label">
                                    GETTING THERE
                                </span>
                                <h2>How to Reach</h2>
                                <p>{details.how_to_reach}</p>
                            </article>
                        </section>
                    )}

                    {details?.facilities && (
                        <section className="place-info-section">
                            <article className="place-card">
                                <span className="section-label">
                                    AT THE DESTINATION
                                </span>
                                <h2>Facilities</h2>
                                <p>{details.facilities}</p>
                            </article>
                        </section>
                    )}
                </div>

                {/* Tickets */}
                {details?.ticket_url && (
                    <section className="ticket-section">
                        <div>
                            <span className="section-label">TICKETS</span>
                            <h2>Ready to plan?</h2>
                            <p>
                                Check official ticket information before
                                visiting.
                            </p>
                        </div>

                        <a
                            href={details.ticket_url}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="ticket-button"
                        >
                            View Official Tickets →
                        </a>
                    </section>
                )}

                {/* Back */}
                <div className="place-back">
                    <Link
                        to={`/country/${countryId}/state/${stateId}`}
                        className="back-link"
                    >
                        ← Back to State
                    </Link>
                </div>
            </div>
        </main>
    );
}

export default Place;