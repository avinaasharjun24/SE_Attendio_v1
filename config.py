import os
import secrets

from dotenv import load_dotenv

load_dotenv()


class Config:
    DEBUG = os.getenv("FLASK_DEBUG", "True").lower() == "true"
    # Generate a strong fallback key for local development if no environment secret is provided.
    SECRET_KEY = os.getenv("SECRET_KEY") or secrets.token_urlsafe(32)
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY") or SECRET_KEY
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_EXPIRATION_HOURS = int(os.getenv("JWT_EXPIRATION_HOURS", "24"))
    JWT_ISSUER = os.getenv("JWT_ISSUER", "attendio-auth")
    BCRYPT_LOG_ROUNDS = int(os.getenv("BCRYPT_LOG_ROUNDS", "12"))
    FACE_MATCH_THRESHOLD = float(os.getenv("FACE_MATCH_THRESHOLD", "0.48"))
    FACE_CONFIDENCE_MIN = float(os.getenv("FACE_CONFIDENCE_MIN", "0.55"))
    FACE_DETECTION_MODEL = os.getenv("FACE_DETECTION_MODEL", "hog")
    ATTENDANCE_LATE_THRESHOLD_MINUTES = int(
        os.getenv("ATTENDANCE_LATE_THRESHOLD_MINUTES", "10")
    )
    LOW_ATTENDANCE_THRESHOLD = float(os.getenv("LOW_ATTENDANCE_THRESHOLD", "75"))

    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "password")
    MYSQL_DB = os.getenv("MYSQL_DB", "attendance_system")
