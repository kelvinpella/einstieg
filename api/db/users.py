from .database import supabase
from ..models.user import NearbyUser


class DbUsers:
    def __init__(self) -> None:
        self.supabase = supabase

    def get_nearby_users(self, user_id: str):
        """
        Retrieve a list of nearby users for the given user_id.
        """
        response = self.supabase.rpc(
            "get_nearby_users",
            {
                "p_user_id": user_id,
                # "p_radius_meters":500 defaults to 500 meters
            },
        ).execute()

        return [NearbyUser(**user) for user in response.data]
