from fastapi import APIRouter
from supabase_auth import User

from api.errors import InternalServerError

from ..db.locations import DbLocations
from ..dependencies import authenticated_user_dependency
from ..models.location import Coordinates, UserLocation

router = APIRouter(prefix="/locations")

db_locations = DbLocations()


@router.post("/update_user_location", response_model=UserLocation)
def update_user_location(
    coordinates: Coordinates, user: User = authenticated_user_dependency
):
    try:
        updated_location = db_locations.add_or_update_user_location(
            user.id, coordinates.latitude, coordinates.longitude
        )
        return updated_location
    except Exception as e:
        raise InternalServerError(message=f"Something went wrong. {str(e)}")
