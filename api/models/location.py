from pydantic import BaseModel 

from ..models.user import Coordinates


class UserLocation(BaseModel):
    user_id: str
    coordinates: Coordinates
