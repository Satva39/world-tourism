from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.health import router as health_router
from app.api.routes.countries import router as countries_router
from app.api.routes.regions import router as regions_router
from app.api.routes.places import router as places_router
from app.core.config import settings
from app.api.routes.place_details import router as place_details_router
from app.api.routes.search import router as search_router
from fastapi.staticfiles import StaticFiles
from app.api.routes.travel import router as travel_router
from pathlib import Path

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
)

STATIC_DIR = Path(__file__).parent / "static"

app.mount(
    "/images",
    StaticFiles(directory="app/static/images"),
    name="images",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(health_router)

app.include_router(
    countries_router,
    prefix="/api",
)

app.include_router(regions_router)
app.include_router(place_details_router)
app.include_router(search_router)
app.include_router(travel_router)

app.include_router(
    places_router,
    prefix="/api",
)


@app.get("/")
def root():
    return {
        "name": settings.app_name,
        "status": "running",
    }
