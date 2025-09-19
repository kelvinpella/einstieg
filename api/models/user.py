from pydantic import BaseModel

from api.models.location import UserLocation


class NearbyUser(BaseModel):
    user_location: UserLocation
    distance: float
