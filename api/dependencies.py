from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from supabase import Client
from .db.client import create_supabase_client


security = HTTPBearer()
supabase: Client = create_supabase_client()


def verify_jwt(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]):
    """
    Verifies the provided JWT access token using Supabase authentication.

    Args:
        credentials (HTTPAuthorizationCredentials): The HTTP authorization credentials containing the JWT token.

    Returns:
        user: The user object returned by Supabase if the token is valid.

    Raises:
        HTTPException: If the token is invalid or an error occurs during verification, raises a 401 Unauthorized error.
    """
    token = credentials.credentials
    try:
        user = supabase.auth.get_user(token)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user

    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))