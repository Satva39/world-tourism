import { useEffect, useMemo, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { getImageUrl } from "../utils/imageUrl";

function State() {
    const { countryId, stateId } = useParams();

    const [region, setRegion] = useState(null);
    const [places, setPlaces] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");
    const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

    useEffect(() => {
        let cancelled = false;

        async function fetchState() {
            try {
                setLoading(true);
                setError("");

                const [regionResponse, placesResponse] =
                    await Promise.all([
                        fetch(`${API_BASE_URL}/regions/${stateId}`),
                        fetch(`${API_BASE_URL}/places/region/${stateId}`),
                    ]);

                if (!regionResponse.ok) {
                    throw new Error(
                        `Could not load region (${regionResponse.status})`
                    );
                }

                if (!placesResponse.ok) {
                    throw new Error(
                        `Could not load famous places (${placesResponse.status})`
                    );
                }

                const regionData = await regionResponse.json();
                const placesData = await placesResponse.json();

                if (!cancelled) {
                    setRegion(regionData);
                    setPlaces(
                        Array.isArray(placesData)
                            ? placesData
                            : placesData.places || []
                    );
                }
            } catch (err) {
                if (!cancelled) {
                    setError(
                        err instanceof Error
                            ? err.message
                            : "Could not load this destination."
                    );
                }
            } finally {
                if (!cancelled) {
                    setLoading(false);
                }
            }
        }

        fetchState();

        return () => {
            cancelled = true;
        };
    }, [stateId]);

    const regionLabel = useMemo(() => {
        const type = String(
            region?.region_type || region?.type || ""
        ).toLowerCase();

        return [
            "ut",
            "union_territory",
            "union-territory",
            "union territory",
        ].includes(type)
            ? "Union Territory"
            : "State";
    }, [region]);

    if (loading) {
        return (
            <main className="state-page">
                <div className="state-container">
                    <div className="page-message">
                        Loading destination...
                    </div>
                </div>
            </main>
        );
    }

    if (error || !region) {
        return (
            <main className="state-page">
                <div className="state-container">
                    <div className="error-card">
                        <span className="section-label">
                            TRAVEL ERROR
                        </span>

                        <h1>Something went wrong</h1>

                        <p>
                            {error ||
                                "This destination could not be found."}
                        </p>

                        <Link
                            to={`/country/${countryId}`}
                            className="back-link"
                        >
                            ← Back to Country
                        </Link>
                    </div>
                </div>
            </main>
        );
    }

    return (
        <main className="state-page">
            <div className="state-container">

                {/* Breadcrumb */}
                <nav
                    className="breadcrumb"
                    aria-label="Breadcrumb"
                >
                    <Link to="/">Home</Link>
                    <span>/</span>

                    <Link to={`/country/${countryId}`}>
                        Country
                    </Link>

                    <span>/</span>

                    <strong>{region.name}</strong>
                </nav>

                {/* Hero */}
                <section className="state-hero">
                    <span className="section-label">
                        DESTINATION
                    </span>

                    <h1>{region.name}</h1>

                    <p>
                        Discover the most remarkable places,
                        attractions, landmarks, and experiences
                        in {region.name}.
                    </p>

                    <div className="state-hero__meta">
                        <span className="state-type">
                            {regionLabel}
                        </span>

                        <span className="state-hero__count">
                            {places.length} destinations
                        </span>
                    </div>
                </section>

                {/* Famous Places */}
                <section className="places-section">
                    <div className="section-heading">
                        <div>
                            <span className="section-label">
                                DISCOVER
                            </span>

                            <h2>
                                Famous Places in {region.name}
                            </h2>
                        </div>

                        <p>
                            Explore the most remarkable destinations,
                            attractions, landmarks, and natural wonders
                            of {region.name}.
                        </p>
                    </div>

                    {places.length === 0 ? (
                        <p className="page-message">
                            No famous places found.
                        </p>
                    ) : (
                        <div className="places-grid">
                            {places.map((place, index) => (
                                <Link
                                    key={place.id}
                                    to={`/country/${countryId}/state/${stateId}/place/${place.id}`}
                                    className="place-card"
                                >
                                    <div className="place-card__image">
                                        {place.cover_image ? (
                                            <img
                                                src={getImageUrl(place.cover_image)}
                                                alt={place.name}
                                                className="place-card__image-img"
                                                loading="lazy"
                                            />
                                        ) : (
                                            <div className="place-card__image-placeholder">
                                                <span>No image yet</span>
                                            </div>
                                        )}

                                        <span className="place-card__number">
                                            {String(index + 1).padStart(2, "0")}
                                        </span>

                                        <span className="place-card__badge">
                                            Explore
                                        </span>
                                    </div>

                                    <div className="place-card__content">
                                        <h3>{place.name}</h3>

                                        {place.short_description && (
                                            <p>{place.short_description}</p>
                                        )}

                                        <span className="place-card__action">
                                            View destination →
                                        </span>
                                    </div>
                                </Link>
                            ))}
                        </div>
                    )}
                </section>

                {/* Back */}
                <Link
                    to={`/country/${countryId}`}
                    className="back-link state-back-link"
                >
                    ← Back to {regionLabel === "State"
                        ? "Country"
                        : "Country"}
                </Link>
            </div>
        </main>
    );
}

export default State;