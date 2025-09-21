from supabase import Client, create_client
from dotenv import load_dotenv
import os

load_dotenv()

# The SUPABASE_URL and SUPABASE_KEY are loaded from environment variables and are used only in the static method to create the client.
# They do not need to be class attributes, as they are not meant to be shared or mutated at the class level, and are not used elsewhere.
SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]
# SUPABASE_SERVICE_ROLE_KEY = os.environ["SUPABASE_SERVICE_ROLE_KEY"]


supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
