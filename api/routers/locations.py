from fastapi import APIRouter, HTTPException
from supabase_auth import User

from ..dependencies import authenticated_user_dependency

from ..db.locations import DbLocations

from ..models.location import UserLocation

from ..models.user import Coordinates


router = APIRouter(prefix="/locations")


@router.post("/update_user_location", response_model=UserLocation)
def update_user_location(
    coordinates: Coordinates, user: User = authenticated_user_dependency
):
    try:
        updated_location = DbLocations.store_user_location(
            user.id, coordinates.latitude, coordinates.longitude
        )
        return updated_location
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
