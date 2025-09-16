from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from supabase import Client
from .db.client import DbClient


class Dependencies:
    # Both 'security' and 'supabase' are used as shared dependencies/resources and do not require per-instance state,
    # so they are best defined as class attributes.
    security = HTTPBearer()
    supabase: Client = DbClient.create_supabase_client()

    @classmethod
    def verify_jwt(
        cls,
        credentials: HTTPAuthorizationCredentials = Depends(security),
    ):
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
            user_response = cls.supabase.auth.get_user(token)
            if not user_response:
                raise HTTPException(status_code=401, detail="Invalid token")
            return user_response.user
        except Exception as e:
            raise HTTPException(status_code=401, detail=str(e))


authenticated_user_dependency = Depends(Dependencies.verify_jwt)
