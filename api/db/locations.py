from typing import Any, Dict

from .database import supabase
from ..models.location import UserLocation


class DbLocations:
    def __init__(self) -> None:
        self.supabase = supabase

    def supabase_rpc_single_data(self, rpc_name: str, params: Dict[Any, Any]):
        """Call a Supabase RPC and return the single result's data."""
        result = self.supabase.rpc(rpc_name, params).single().execute()
        return result.data

    def get_user_location(self, user_id: str):
        """Retrieve the location of a user by user_id."""
        data = self.supabase_rpc_single_data(
            "get_user_location", {"p_user_id": user_id}
        )
        return UserLocation(**data)

    def add_or_update_user_location(
        self, user_id: str, latitude: float, longitude: float
    ):
        """Add or update a user's location and return the updated UserLocation."""
        data = self.supabase_rpc_single_data(
            "add_or_update_user_location",
            {
                "p_user_id": user_id,
                "p_latitude": latitude,
                "p_longitude": longitude,
            },
        )
        
        return UserLocation(**{**data, "user_id": data["returned_user_id"]})
