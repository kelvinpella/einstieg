from ..models.user import NearbyUser
from .client import DbClient


class DbUsers(DbClient):
    @classmethod
    def get_nearby_users(cls, user_id: str):
        """
        Retrieve a list of nearby users for the given user_id.
        """
        response = cls.supabase.rpc(
            "get_nearby_users",
            {
                "p_user_id": user_id,
                # "p_radius_meters":500 defaults to 500 meters
            },
        ).execute()

        return [NearbyUser(**user) for user in response.data]
