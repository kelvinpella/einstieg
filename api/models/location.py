from pydantic import BaseModel, model_validator

from api.errors import PydanticRequestValidationError


class Coordinates(BaseModel):
    latitude: float
    longitude: float

    @model_validator(mode="after")
    def check_coordinates(self):
        if self.latitude is None or self.longitude is None:
            raise PydanticRequestValidationError(
                message="Latitude and longitude are required"
            )
        return self


class UserLocation(Coordinates):
    id: str
    user_id: str
    created_at: str
    updated_at: str
