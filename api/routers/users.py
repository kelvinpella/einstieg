from typing import List
from fastapi import APIRouter, HTTPException
from supabase_auth import User
from ..db.users import DbUsers
from ..dependencies import authenticated_user_dependency
from ..models.user import NearbyUser


router = APIRouter(prefix="/users", dependencies=[authenticated_user_dependency])


@router.get("/nearby_users", response_model=List[NearbyUser])
def get_nearby_users(
    user: User = authenticated_user_dependency,
) -> List[NearbyUser]:
    try:
        users = DbUsers.get_nearby_users(user_id=user.id)
        return users
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
