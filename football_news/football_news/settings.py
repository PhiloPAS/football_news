# Tambahkan import ini di bagian atas file (setelah import Path)
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Modifikasi ALLOWED_HOSTS menjadi:
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "<URL deployment PWS kamu>"]

# Tambahkan konfigurasi PRODUCTION tepat di atas DEBUG:
PRODUCTION = os.getenv('PRODUCTION', 'False').lower() == 'true'

# Ganti konfigurasi DATABASES dengan:
# Database configuration
if PRODUCTION:
    # Production: gunakan PostgreSQL dengan kredensial dari environment variables
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
            'OPTIONS': {
                'options': f"-c search_path={os.getenv('SCHEMA', 'public')}"
            }
        }
    }
else:
    # Development: gunakan SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }