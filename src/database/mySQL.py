from database.config import Settings

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL


engine = create_engine(URL.create(
    "mysql+pymysql",
    username=Settings.MYSQL_USERNAME,
    password=Settings.MYSQL_PSWD,
    port=Settings.MYSQL_PORT,
    host=Settings.MYSQL_HOST,
    database=Settings.MYSQL_DATABASE,
))

Session = sessionmaker(bind=engine)

def get_session():
    return Session()

def get_engine():
    return engine
