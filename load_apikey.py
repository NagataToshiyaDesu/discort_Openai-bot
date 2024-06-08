from dotenv import load_dotenv
import os
def get_apikey() -> str:
    """
    This method return API_KEY
    """
    load_dotenv(".env")
    return os.getenv("OPENAI_API_KEY")