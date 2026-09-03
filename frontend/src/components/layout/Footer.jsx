function Footer() {
    return (
        <footer className="site-footer">
            <div className="site-footer__inner">
                <div>
                    <h3>World Tourism</h3>
                    <p>
                        Discover countries, explore regions, and find
                        remarkable places around the world.
                    </p>
                </div>

                <div className="site-footer__bottom">
                    <span>
                        © {new Date().getFullYear()} World Tourism
                    </span>

                    <span>Explore. Discover. Remember.</span>
                </div>
            </div>
        </footer>
    );
}

export default Footer;