from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from .errors import InternalServerError, InvalidToken

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
            raise InvalidToken(message="Invalid token")
        return user_response.user
    except InvalidToken:
        raise
    except Exception as e:
        raise InternalServerError(message=f"Something went wrong. {str(e)}")


authenticated_user_dependency = Depends(verify_jwt)
