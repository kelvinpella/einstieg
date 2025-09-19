from supabase import Client
from ..models.user import NearbyUser
from .client import DbClient


class DbUsers:
    supabase: Client = DbClient.create_supabase_client()

    @classmethod
    def get_nearby_users(cls, user_id: str):
        response = cls.supabase.rpc(
            "get_nearby_users",
            {
                "p_user_id": user_id,
                # "p_radius_meters":500 defaults to 500 meters
            },
        ).execute()

        return [NearbyUser(**user) for user in response.data]
