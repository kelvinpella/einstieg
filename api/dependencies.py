from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from supabase import Client
from supabase_auth import UserResponse
from .db.client import create_supabase_client


security = HTTPBearer()
supabase: Client = create_supabase_client()


def verify_jwt(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
) -> UserResponse:
    """
    Verifies the provided JWT access token using Supabase authentication.

    Args:
        credentials (HTTPAuthorizationCredentials): The HTTP authorization credentials containing the JWT token.

    Returns:
        user_response: The user_response object returned by Supabase if the token is valid.

    Raises:
        HTTPException: If the token is invalid or an error occurs during verification, raises a 401 Unauthorized error.
    """
    token = credentials.credentials
    try:
        user_response = supabase.auth.get_user(token)
        if not user_response:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user_response

    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
