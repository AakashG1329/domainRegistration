# import MySQLdb  
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Update the MySQL database URL
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost/domain_registration"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()