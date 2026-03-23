import json
import os

def get_credentials():
    """Gets credentials from environment variables stored in a private .env.json file."""

    env_file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_file_dir = os.path.join(env_file_dir, "FlashyCards")
    with open(os.path.join(env_file_dir, '.env.json'), 'r') as f:
        creds = json.loads(f.read())
    return creds


credentials = get_credentials()