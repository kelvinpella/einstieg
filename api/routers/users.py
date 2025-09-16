from typing import List
from fastapi import APIRouter, HTTPException
from supabase_auth import User
from ..dependencies import authenticated_user_dependency
from ..db.locations import DbLocations
from ..services.user_service import UserService
from ..models.user import NearbyUser


router = APIRouter(prefix="/users", dependencies=[authenticated_user_dependency])


@router.get("/nearby_users", response_model=List[NearbyUser])
def get_nearby_users(
    user: User = authenticated_user_dependency,
) -> List[NearbyUser]:
    try:
        user_location = DbLocations.get_user_location(user.id)
        nearby_users = UserService.filter_nearby_users(**user_location.__dict__)
        return nearby_users
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
