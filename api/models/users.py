from pydantic import BaseModel


class Coordinates(BaseModel):
    latitude: float
    longitude: float


class NearbyUser(BaseModel):
    user_id: str
    name: str
    distance: float
    coordinates: Coordinates
