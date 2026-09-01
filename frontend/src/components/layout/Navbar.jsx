import { Link } from "react-router-dom";

function Navbar() {
    return (
        <header>
            <nav>
                <Link to="/">
                    World Tourism
                </Link>

                <div>
                    <Link to="/">Home</Link>
                </div>
            </nav>
        </header>
    );
}

export default Navbar;