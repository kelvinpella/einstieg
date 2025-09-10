from typing import Annotated
from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from supabase import Client
from .db.client import create_supabase_client


security = HTTPBearer()
supabase: Client = create_supabase_client()


def verify_jwt(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]):
    token = credentials.credentials
    print("verify_jwt",token)
