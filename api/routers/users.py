from typing import List
from fastapi import APIRouter, Depends, HTTPException
from supabase_auth.types import UserResponse
from ..dependencies import verify_jwt
from ..models.users import Coordinates, NearbyUser

authenticated_user_dependency = Depends(verify_jwt)

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
        return [
            NearbyUser(
                user_id=user.id,
                name="kelvin",
                distance=45.5,
                coordinates=Coordinates(latitude=34.6, longitude=45.8),
            )
        ]
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
