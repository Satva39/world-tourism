from pydantic import BaseModel


class RegionResponse(BaseModel):
    id: int
    country_id: int
    name: str
    slug: str
    region_type: str

    model_config = {
        "from_attributes": True,
    }
