from pydantic import BaseModel


class Coordinates(BaseModel):
    latitude: float
    longitude: float


class NearbyUser(BaseModel):
    userId: str
    name: str
    distance: float
    coordinates: Coordinates
