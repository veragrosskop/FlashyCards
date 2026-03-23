import json
import os

def get_credentials():
    """Gets credentials from environment variables stored in a private .env.json file."""

    try:
        env_file_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        env_file_dir = os.path.join(env_file_dir, "FlashyCards")
        with open(os.path.join(env_file_dir, '.env.json'), 'r') as f:
            creds = json.loads(f.read())
        return creds
    except FileNotFoundError:
        return {
            "debug": os.environ.get("DEBUG", "False") == "True",
            "allowed_hosts": os.environ.get("ALLOWED_HOSTS", "").split(","),
            "django_secret_key": os.environ.get("DJANGO_SECRET_KEY"),
            "db_password": os.environ.get("DB_PASSWORD"),
            "db_name": os.environ.get("DB_NAME"),
            "db_user": os.environ.get("DB_USER"),
            "db_host": os.environ.get("DB_HOST"),
        }


credentials = get_credentials()