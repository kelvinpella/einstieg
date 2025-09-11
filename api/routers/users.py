from typing import List
from fastapi import APIRouter, Depends
from ..dependencies import verify_jwt
from ..models.users import NearbyUser

authenticated_user = Depends(verify_jwt)

router = APIRouter(prefix="/users", dependencies=[authenticated_user])


@router.get("/nearby_users/{user_id}", response_model=List[NearbyUser])
def get_nearby_users(user_id: str): 
    return [
        {
            "user_id": user_id,
            "name": "Kelvin",
            "distance": 25,
            "coordinates": {"latitude": 24.56, "longitude": 45.43},
        }
    ]
