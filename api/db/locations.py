from supabase import Client
from ..models.location import UserLocation
from .client import DbClient


class DbLocations:
    @staticmethod
    def get_user_location(user_id: str):
        supabase: Client = DbClient.create_supabase_client()
        result = (
            supabase.table("locations").select("*").eq("user_id", user_id).execute()
        )
        data = result.data
        return UserLocation(**data[0])

    @staticmethod
    def add_or_update_user_location(user_id: str, latitude: float, longitude: float):
        supabase: Client = DbClient.create_supabase_client()
        response = (
            supabase.rpc(
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
