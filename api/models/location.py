from pydantic import BaseModel


class UserLocation(BaseModel):
    id: str
    user_id: str
    latitude: float
    longitude: float
    created_at: str
    updated_at: str
