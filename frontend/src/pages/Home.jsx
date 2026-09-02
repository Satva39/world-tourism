import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { getImageUrl } from "../utils/imageUrl";
import SearchBar from "../components/SearchBar";

function Home() {
    const [countries, setCountries] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");
    const [featuredPlaces, setFeaturedPlaces] = useState([]);
    const [featuredLoading, setFeaturedLoading] = useState(true);
    const [featuredError, setFeaturedError] = useState("");

    useEffect(() => {
        async function fetchCountries() {
            try {
                setLoading(true);
                setError("");

                const response = await fetch(
                    `${import.meta.env.VITE_API_BASE_URL}/countries`,
                );

                if (!response.ok) {
                    throw new Error("Countries could not be loaded");
                }

                const data = await response.json();
                setCountries(data);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        }

        fetchCountries();
    }, []);

    useEffect(() => {
        let cancelled = false;

        async function fetchFeaturedPlaces() {
            try {
                setFeaturedLoading(true);
                setFeaturedError("");

                const response = await fetch(
                    `${import.meta.env.VITE_API_BASE_URL}/places/featured`
                );

                if (!response.ok) {
                    throw new Error(
                        `Could not load featured places (${response.status})`
                    );
                }

                const data = await response.json();

                if (!cancelled) {
                    setFeaturedPlaces(
                        Array.isArray(data) ? data : []
                    );
                }
            } catch (err) {
                if (!cancelled) {
                    setFeaturedError(
                        err instanceof Error
                            ? err.message
                            : "Could not load featured places."
                    );
                }
            } finally {
                if (!cancelled) {
                    setFeaturedLoading(false);
                }
            }
        }

        fetchFeaturedPlaces();

        return () => {
            cancelled = true;
        };
    }, []);

    return (
        <main className="home-page">
            <section className="home-hero">
                <div className="container">
                    <div className="hero-content">
                        <span className="hero-eyebrow">
                            EXPLORE THE WORLD
                        </span>

                        <h1>
                            Discover places
                            <br />
                            worth remembering.
                        </h1>

                        <p>
                            Explore countries, discover their states and
                            regions, and find the world's most remarkable
                            destinations.
                        </p>
                        <SearchBar />
                    </div>
                </div>
            </section>

            <section className="countries-section container">
                <div className="section-heading">
                    <div>
                        <span className="section-eyebrow">
                            DESTINATIONS
                        </span>

                        <h2>Explore Countries</h2>
                    </div>

                    <p>
                        Choose a country to begin your journey.
                    </p>
                </div>

                {loading && (
                    <div className="loading">
                        Loading countries...
                    </div>
                )}

                {error && (
                    <div className="error">
                        <h3>Something went wrong</h3>
                        <p>{error}</p>
                    </div>
                )}

                {!loading && !error && countries.length === 0 && (
                    <div className="empty">
                        <p>No countries found.</p>
                    </div>
                )}

                {!loading && !error && countries.length > 0 && (
                    <div className="country-grid">
                        {countries.map((country) => (
                            <Link
                                key={country.id}
                                to={`/country/${country.id}`}
                                className="country-card"
                            >
                                <div className="country-card-content">
                                    <span className="country-code">
                                        {country.iso_code}
                                    </span>

                                    <h3>{country.name}</h3>

                                    <span className="explore-link">
                                        Explore
                                        <span>→</span>
                                    </span>
                                </div>
                            </Link>
                        ))}
                    </div>
                )}
            </section>

            <section className="featured-section">
                <div className="section-heading">
                    <div>
                        <span className="section-label">
                            FEATURED
                        </span>

                        <h2>Places Worth Discovering</h2>
                    </div>

                    <p>
                        Explore some of the destinations waiting
                        to be discovered across India.
                    </p>
                </div>

                {featuredLoading ? (
                    <div className="page-message">
                        Loading featured destinations...
                    </div>
                ) : featuredError ? (
                    <div className="error-card">
                        <span className="section-label">
                            TRAVEL ERROR
                        </span>

                        <p>{featuredError}</p>
                    </div>
                ) : featuredPlaces.length === 0 ? (
                    <div className="page-message">
                        No featured destinations found.
                    </div>
                ) : (
                    <div className="featured-places-grid">
                        {featuredPlaces.map((place) => (
                            <Link
                                key={place.id}
                                to={`/country/${place.country_id}/state/${place.region_id}/place/${place.id}`}
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
                                            <span>Image coming soon</span>
                                        </div>
                                    )}

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

        </main>
    );
}

export default Home;