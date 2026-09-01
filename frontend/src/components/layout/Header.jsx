import { Link } from "react-router-dom";

export default function Header() {
    return (
        <header className="site-header">
            <div className="site-header__inner">
                <Link to="/" className="site-logo">
                    World Tourism
                </Link>

                <nav className="site-nav">
                    <Link to="/" className="site-nav__link">
                        Home
                    </Link>
                </nav>
            </div>
        </header>
    );
}