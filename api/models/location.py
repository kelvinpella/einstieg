from pydantic import BaseModel


class UserLocation(BaseModel):
    user_id: str
    latitude: float
    longitude: float
