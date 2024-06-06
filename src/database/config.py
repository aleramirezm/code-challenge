import structlog
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

class Settings():
    """Class that handles enviroment variables"""
    
    MYSQL_USERNAME = os.getenv("MYSQL_USERNAME")
    MYSQL_PSWD = os.getenv("MYSQL_PSWD")
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
    MYSQL_PORT = os.getenv("MYSQL_PORT")

settings = Settings()

log = structlog.get_logger()