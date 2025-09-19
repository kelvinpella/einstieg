from pydantic import BaseModel


class Coordinates(BaseModel):
    latitude: float
    longitude: float


class UserLocation(Coordinates):
    id: str
    user_id: str
    created_at: str
    updated_at: str
