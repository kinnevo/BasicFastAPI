from app.config import get_settings

settings = get_settings()
print(f"MongoDB URL: {settings.mongodb_url}")
print(f"Database Name: {settings.database_name}")
print(f"Secret Key is set: {'Yes' if settings.secret_key else 'No'}") 