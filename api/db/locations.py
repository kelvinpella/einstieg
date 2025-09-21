from typing import Any, Dict
from ..models.location import UserLocation
from .client import DbClient


class DbLocations(DbClient):
    @classmethod
    def supabase_rpc_single_data(cls, rpc_name: str, params: Dict[Any, Any]):
        """Call a Supabase RPC and return the single result's data."""
        result = cls.supabase.rpc(rpc_name, params).single().execute()
        return result.data

    @classmethod
    def get_user_location(cls, user_id: str):
        """Retrieve the location of a user by user_id."""
        data = cls.supabase_rpc_single_data("get_user_location", {"p_user_id": user_id})
        return UserLocation(**data)

    @classmethod
    def add_or_update_user_location(
        cls, user_id: str, latitude: float, longitude: float
    ):
        """Add or update a user's location and return the updated UserLocation."""
        data = cls.supabase_rpc_single_data(
            "add_or_update_user_location",
            {
                "p_user_id": user_id,
                "p_latitude": latitude,
                "p_longitude": longitude,
            },
        )
        return UserLocation(**{**data, "user_id": data["returned_user_id"]})
