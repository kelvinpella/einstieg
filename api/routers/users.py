from typing import List
from fastapi import APIRouter
from supabase_auth import User
from ..errors import InternalServerError
from ..db.users import DbUsers
from ..dependencies import authenticated_user_dependency
from ..models.user import NearbyUser


router = APIRouter(prefix="/users")

db_users = DbUsers()


@router.get("/nearby_users", response_model=List[NearbyUser])
def get_nearby_users(
    user: User = authenticated_user_dependency,
) -> List[NearbyUser]:
    """
    Retrieve a list of nearby users for the authenticated user.

    Args:
        user (User): The currently authenticated user.

    Returns:
        List[NearbyUser]: A list of users who are nearby the authenticated user.

    Raises:
        HTTPException: If an error occurs while retrieving nearby users.
    """
    try:
        users = db_users.get_nearby_users(user.id)
        return users
    except Exception as e:
        raise InternalServerError(message=f"Something went wrong. {str(e)}")
