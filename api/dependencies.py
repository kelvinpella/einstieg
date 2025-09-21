from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from .db.database import supabase

security = HTTPBearer()


def verify_jwt(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Verifies the provided JWT access token using Supabase authentication.

    Args:
        credentials (HTTPAuthorizationCredentials): The HTTP authorization credentials containing the JWT access token.

    Returns:
        User: The user information associated with the valid JWT token.

    Raises:
        HTTPException: If the token is invalid or verification fails.
    """
    token = credentials.credentials
    try:
        user_response = supabase.auth.get_user(token)
        if not user_response:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user_response.user
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))


authenticated_user_dependency = Depends(verify_jwt)
