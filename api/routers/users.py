from typing import List
from fastapi import APIRouter, Depends, HTTPException
from supabase_auth.types import UserResponse
from ..dependencies import Dependencies
from ..services.user_service import UserService
from ..models.user import Coordinates, NearbyUser

authenticated_user_dependency = Depends(Dependencies.verify_jwt)

router = APIRouter(prefix="/users", dependencies=[authenticated_user_dependency])


@router.get("/nearby_users", response_model=List[NearbyUser])
def get_nearby_users(
    user_response: UserResponse = authenticated_user_dependency,
) -> List[NearbyUser]:
    try:
        user = user_response.user
        if "coordinates" not in user.user_metadata:
            raise HTTPException(
                status_code=404, detail="Coordinates not found in user metadata"
            )
        coordinates = Coordinates(**user.user_metadata["coordinates"])
        nearby_users =UserService.filter_nearby_users(**coordinates.__dict__)
        return nearby_users
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
