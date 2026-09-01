from pydantic import BaseModel


class CountryResponse(BaseModel):
    id: int
    name: str
    slug: str
    iso_code: str

    model_config = {
        "from_attributes": True,
    }
