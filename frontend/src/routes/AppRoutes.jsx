import { Routes, Route } from "react-router-dom";

import Home from "../pages/Home";
import Country from "../pages/Country";
import State from "../pages/State";
import Place from "../pages/Place";
import NotFound from "../pages/NotFound";

function AppRoutes() {
    return (
        <Routes>
            <Route path="/" element={<Home />} />

            <Route
                path="/country/:countryId"
                element={<Country />}
            />

            <Route
                path="/country/:countryId/state/:stateId"
                element={<State />}
            />

            <Route
                path="/country/:countryId/state/:stateId/place/:placeId"
                element={<Place />}
            />

            <Route path="*" element={<NotFound />} />
        </Routes>
    );
}

export default AppRoutes;