from typing import List
from fastapi import APIRouter, Depends
from ..dependencies import verify_jwt
from ..models.users import NearbyUser

authenticated_user = Depends(verify_jwt)

router = APIRouter(prefix="/users", dependencies=[authenticated_user])

@router.get("/nearby_users/{user_id}", response_model=List[NearbyUser])
def get_nearby_users(user_id: str):
    print("nearby_user",user_id)
