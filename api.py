"""
api.py: Fetches data from an external API
"""
import requests

API_URL = "https://devapi.beyondchats.com/api/get_message_with_sources"

def fetch_data(page=1):
    """
    Fetch data from the external API with pagination.

    Args:
        page (int): The page number to fetch.

    Returns:
        dict: The JSON response from the API if successful, None otherwise.
    """
    response = requests.get(f"{API_URL}?page={page}")
    if response.status_code == 200:
        return response.json()
    return None
