from supabase import Client
from ..models.location import UserLocation
from .client import DbClient


class DbLocations:
    supabase: Client = DbClient.create_supabase_client()

    @classmethod
    def get_user_location(cls, user_id: str):
        result = (
            cls.supabase.rpc("get_user_location", {"p_user_id": user_id})
            .single()
            .execute()
        )
        data = result.data
        return UserLocation(**data)

    @classmethod
    def add_or_update_user_location(
        cls, user_id: str, latitude: float, longitude: float
    ):
        response = (
            cls.supabase.rpc(
                "add_or_update_user_location",
                {
                    "p_user_id": user_id,
                    "p_latitude": latitude,
                    "p_longitude": longitude,
                },
            )
            .single()
            .execute()
        )
        data = response.data
        return UserLocation(**{**data, "user_id": data["returned_user_id"]})
