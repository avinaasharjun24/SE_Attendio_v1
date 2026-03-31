from config import Config


class DatabaseConfig:
    HOST = Config.MYSQL_HOST
    PORT = Config.MYSQL_PORT
    USER = Config.MYSQL_USER
    PASSWORD = Config.MYSQL_PASSWORD
    DATABASE = Config.MYSQL_DB

    @classmethod
    def admin_connection_settings(cls):
        # Connect without selecting a DB first so the app can create it if needed.
        return {
            "host": cls.HOST,
            "port": cls.PORT,
            "user": cls.USER,
            "password": cls.PASSWORD,
            "autocommit": True,
        }

    @classmethod
    def app_connection_settings(cls):
        return {
            "host": cls.HOST,
            "port": cls.PORT,
            "user": cls.USER,
            "password": cls.PASSWORD,
            "database": cls.DATABASE,
            "autocommit": False,
        }
