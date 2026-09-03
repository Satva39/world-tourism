import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";

const regionImages = {
    "Andhra Pradesh": "/images/states/andhra-pradesh.jpg",
    "Arunachal Pradesh": "/images/states/arunachal-pradesh.jpg",
    "Assam": "/images/states/assam.gif",
    "Bihar": "/images/states/bihar.webp",
    "Chhattisgarh": "/images/states/chhattisgarh.jpg",
    "Goa": "/images/states/goa.jpg",
    "Gujarat": "/images/states/gujarat.jpg",
    "Haryana": "/images/states/haryana.png",
    "Himachal Pradesh": "/images/states/himachal-pradesh.gif",
    "Jharkhand": "/images/states/jharkhand.jpg",
    "Karnataka": "/images/states/karnataka.jpg",
    "Kerala": "/images/states/kerala.gif",
    "Madhya Pradesh": "/images/states/madhya-pradesh.jpg",
    "Maharashtra": "/images/states/maharashtra.jpg",
    "Manipur": "/images/states/manipur.jpg",
    "Meghalaya": "/images/states/meghalaya.jpg",
    "Mizoram": "/images/states/mizoram.png",
    "Nagaland": "/images/states/nagaland.gif",
    "Odisha": "/images/states/odisha.png",
    "Punjab": "/images/states/punjab.png",
    "Rajasthan": "/images/states/rajasthan.jpg",
    "Sikkim": "/images/states/sikkim.png",
    "Tamil Nadu": "/images/states/tamil-nadu.jpg",
    "Telangana": "/images/states/telangana.jpg",
    "Tripura": "/images/states/tripura.jpg",
    "Uttar Pradesh": "/images/states/uttar-pradesh.jpg",
    "Uttarakhand": "/images/states/uttarakhand.webp",
    "West Bengal": "/images/states/west-bengal.jpg",
    "Andaman and Nicobar Islands": "/images/states/andaman-and-nicobar-islands.png",
    "Chandigarh": "/images/states/chandigarh.png",
    "Dadra and Nagar Haveli and Daman and Diu": "/images/states/dadra-and-nagar-haveli-and-daman-and-diu.jpg",
    "Delhi": "/images/states/delhi.avif",
    "Jammu and Kashmir": "/images/states/jammu-and-kashmir.gif",
    "Ladakh": "/images/states/ladakh.jpg",
    "Lakshadweep": "/images/states/lakshadweep.png",
    "Puducherry": "/images/states/puducherry.jpg"
};

function Country() {
    const { countryId } = useParams();

    const [country, setCountry] = useState(null);
    const [regions, setRegions] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {
        async function fetchCountry() {
            try {
                setLoading(true);
                setError("");

                const [countryResponse, regionsResponse] = await Promise.all([
                    fetch(`${import.meta.env.VITE_API_BASE_URL}/countries/${countryId}`),
                    fetch(`${import.meta.env.VITE_API_BASE_URL}/regions/country/${countryId}`),
                ]);

                if (!countryResponse.ok) {
                    throw new Error("Country not found");
                }

                if (!regionsResponse.ok) {
                    throw new Error("Could not load states and union territories");
                }

                const countryData = await countryResponse.json();
                const regionsData = await regionsResponse.json();

                setCountry(countryData);
                setRegions(regionsData);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        }

        fetchCountry();
    }, [countryId]);

    if (loading) {
        return (
            <main className="country-page">
                <p className="page-message">Loading country...</p>
            </main>
        );
    }

    if (error) {
        return (
            <main className="country-page">
                <div className="error-card">
                    <h1>Something went wrong</h1>
                    <p>{error}</p>
                    <Link to="/" className="back-link">
                        Back to Home
                    </Link>
                </div>
            </main>
        );
    }

    return (
        <main className="country-page">
            <div className="country-container">
                <div className="breadcrumb">
                    <Link to="/">Home</Link>
                    <span>/</span>
                    <span>{country.name}</span>
                </div>

                <section className="country-hero">
                    <span className="section-label">DESTINATION</span>

                    <h1>{country.name}</h1>

                    <p>
                        Explore the states and union territories of{" "}
                        {country.name}, then discover their most famous
                        destinations and attractions.
                    </p>

                    {country.iso_code && (
                        <span className="country-code">
                            ISO Code: {country.iso_code}
                        </span>
                    )}
                </section>

                <section className="regions-section">
                    <div className="section-heading">
                        <div>
                            <span className="section-label">EXPLORE</span>
                            <h2>States & Union Territories</h2>
                        </div>

                        <p>
                            Choose a region to discover its famous places.
                        </p>
                    </div>

                    {regions.length === 0 ? (
                        <p className="page-message">
                            No states or union territories found.
                        </p>
                    ) : (
                        <div className="regions-grid">
                            {regions.map((region, index) => (
                                <Link
                                    key={region.id}
                                    to={`/country/${countryId}/state/${region.id}`}
                                    className="region-card"
                                >
                                    <div className="region-card__image">
                                        {regionImages[region.name] ? (
                                            <img
                                                src={regionImages[region.name]}
                                                alt={region.name}
                                                loading="lazy"
                                            />
                                        ) : (
                                            <div className="region-card__image-placeholder">
                                                <span aria-hidden="true">✦</span>
                                            </div>
                                        )}

                                        <span className="region-number">
                                            {String(index + 1).padStart(2, "0")}
                                        </span>

                                        <span className="region-type">
                                            {String(region.region_type || "")
                                                .trim()
                                                .toLowerCase()
                                                .replace(/[\s-]+/g, "_") === "union_territory"
                                                ? "Union Territory"
                                                : "State"}
                                        </span>
                                    </div>

                                    <div className="region-card__content">
                                        <h3>{region.name}</h3>

                                        <span className="region-action">
                                            Explore places
                                            <span aria-hidden="true">→</span>
                                        </span>
                                    </div>
                                </Link>
                            ))}
                        </div>
                    )}
                </section>
            </div>
        </main>
    );
}

export default Country;