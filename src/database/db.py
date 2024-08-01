import os
# DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy
#  engine = create_engine(DATABASE_URL)
#  metadata = MetaData()

# databases query builder
#  database = Database(DATABASE_URL)


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="",
    host="localhost",
    database="mydb",
    port=5432
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()


session_local = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()