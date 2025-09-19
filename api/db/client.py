from supabase import create_client
from dotenv import load_dotenv
import os
from typing import Literal

load_dotenv()
# The SUPABASE_URL and SUPABASE_KEY are loaded from environment variables and are used only in the static method to create the client.
# They do not need to be class attributes, as they are not meant to be shared or mutated at the class level, and are not used elsewhere.

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]
SUPABASE_SERVICE_ROLE_KEY = os.environ["SUPABASE_SERVICE_ROLE_KEY"]


class DbClient:
    @staticmethod
    def create_supabase_client(keyRole: Literal["anon", "role"] = "anon"):
        """Create and return a Supabase client instance.

        Args:
            keyRole: Which keyRole to use, "anon" or "role". Defaults to "anon".
        """
        return create_client(
            SUPABASE_URL,
            SUPABASE_SERVICE_ROLE_KEY if keyRole == "role" else SUPABASE_KEY,
        )
