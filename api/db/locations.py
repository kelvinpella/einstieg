import os
from supabase import Client
from dotenv import load_dotenv
from ..models.location import UserLocation
from .client import DbClient


load_dotenv()
# The SUPABASE_URL and SUPABASE_KEY are loaded from environment variables and are used only in the static method to create the client.
# They do not need to be class attributes, as they are not meant to be shared or mutated at the class level, and are not used elsewhere.

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]


class DbLocations:
    supabase: Client = DbClient.create_supabase_client()

    @classmethod
    def get_user_location(cls, user_id: str):
        result = (
            cls.supabase.table("locations").select("*").eq("user_id", user_id).execute()
        )
        data = result.data
        print(data)
        # if not data:
        #     raise ValueError("User location not found")
        return UserLocation(**data[0])

    @classmethod
    def store_user_location(cls, user_id: str, latitude: float, longitude: float):
        data = {"user_id": user_id, "location": f"POINT({longitude} {latitude})"}
        response = (
            cls.supabase.table("locations").upsert(data, on_conflict=user_id).execute()
        )
        print(response.data)
        return UserLocation(
            **{"user_id": "Random", "latitude": 45.4, "longitude": 83.9}
        )
