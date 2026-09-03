import { useEffect, useRef, useState } from "react";
import { Link } from "react-router-dom";
import API_BASE_URL from "../config/api";

function SearchBar() {
    const [query, setQuery] = useState("");
    const [results, setResults] = useState({
        countries: [],
        regions: [],
        places: [],
    });
    const [loading, setLoading] = useState(false);
    const [open, setOpen] = useState(false);

    const searchRef = useRef(null);

    useEffect(() => {
        const trimmedQuery = query.trim();

        if (!trimmedQuery) {
            setResults({
                countries: [],
                regions: [],
                places: [],
            });
            setLoading(false);
            return;
        }

        const controller = new AbortController();

        const timer = setTimeout(async () => {
            try {
                setLoading(true);

                const response = await fetch(
                    `${API_BASE_URL}/search?q=${encodeURIComponent(trimmedQuery)}`,
                    {
                        signal: controller.signal,
                    }
                );
                if (!response.ok) {
                    throw new Error("Search failed");
                }

                const data = await response.json();

                setResults({
                    countries: data.countries || [],
                    regions: data.regions || [],
                    places: data.places || [],
                });

                setOpen(true);
            } catch (error) {
                if (error.name !== "AbortError") {
                    console.error("Search error:", error);
                }
            } finally {
                setLoading(false);
            }
        }, 180);

        return () => {
            clearTimeout(timer);
            controller.abort();
        };
    }, [query]);

    useEffect(() => {
        function handleClickOutside(event) {
            if (
                searchRef.current &&
                !searchRef.current.contains(event.target)
            ) {
                setOpen(false);
            }
        }

        document.addEventListener("mousedown", handleClickOutside);

        return () => {
            document.removeEventListener("mousedown", handleClickOutside);
        };
    }, []);

    const hasResults =
        results.countries.length > 0 ||
        results.regions.length > 0 ||
        results.places.length > 0;

    return (
        <div className="search-wrapper" ref={searchRef}>
            <div className="search-box">
                <span className="search-icon">⌕</span>

                <input
                    type="text"
                    value={query}
                    onChange={(event) => {
                        setQuery(event.target.value);
                        setOpen(true);
                    }}
                    onFocus={() => {
                        if (query.trim()) {
                            setOpen(true);
                        }
                    }}
                    placeholder="Search countries, states or places..."
                    aria-label="Search destinations"
                />

                {loading && <span className="search-spinner" aria-label="Searching" />}
            </div>

            {open && query.trim() && (
                <div className="search-results">
                    {loading && (
                        <div className="search-message search-message--loading">
                            <span className="search-spinner" aria-hidden="true" />
                            <span>Searching destinations...</span>
                        </div>
                    )}
                    {!loading && !hasResults && (
                        <div className="search-message">
                            No destinations found.
                        </div>
                    )}

                    {!loading && results.countries.length > 0 && (
                        <div className="search-group">
                            <div className="search-group-title">
                                Countries
                            </div>

                            {results.countries.map((country) => (
                                <Link
                                    key={country.id}
                                    to={`/country/${country.id}`}
                                    className="search-result"
                                    onClick={() => setOpen(false)}
                                >
                                    <div>
                                        <strong>{country.name}</strong>
                                        <span>Country</span>
                                    </div>

                                    <span className="search-arrow">→</span>
                                </Link>
                            ))}
                        </div>
                    )}

                    {!loading && results.regions.length > 0 && (
                        <div className="search-group">
                            <div className="search-group-title">
                                States & Union Territories
                            </div>

                            {results.regions.map((region) => (
                                <Link
                                    key={region.id}
                                    to={`/country/${region.country_id}/state/${region.id}`}
                                    className="search-result"
                                    onClick={() => setOpen(false)}
                                >
                                    <div>
                                        <strong>{region.name}</strong>
                                        <span>
                                            {region.region_type ===
                                                "union_territory"
                                                ? "Union Territory"
                                                : "State"}
                                        </span>
                                    </div>

                                    <span className="search-arrow">→</span>
                                </Link>
                            ))}
                        </div>
                    )}

                    {!loading && results.places.length > 0 && (
                        <div className="search-group">
                            <div className="search-group-title">
                                Famous Places
                            </div>

                            {results.places.map((place) => (
                                <Link
                                    key={place.id}
                                    to={`/country/${place.country_id}/state/${place.region_id}/place/${place.id}`}
                                    className="search-result"
                                    onClick={() => setOpen(false)}
                                >
                                    <div>
                                        <strong>{place.name}</strong>

                                        <span>
                                            {place.short_description}
                                        </span>
                                    </div>

                                    <span className="search-arrow">→</span>
                                </Link>
                            ))}
                        </div>
                    )}
                </div>
            )}
        </div>
    );
}

export default SearchBar;