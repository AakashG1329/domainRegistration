from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# server = "gsmtechinfo.mssql.somee.com"
# user = "aakashg132906_SQLLogin_1"
# password = "8nxdn44l2q"
# db_name = "gsmtechinfo"


# Update the MySQL database URL
# SQLALCHEMY_DATABASE_URL = "workstation id=gsmtechinfo.mssql.somee.com;packet size=4096;user id=aakashg132906_SQLLogin_1;pwd=8nxdn44l2q;data source=gsmtechinfo.mssql.somee.com;persist security info=False;initial catalog=gsmtechinfo;TrustServerCertificate=True"
#SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:@localhost/domain_registration"
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://if0_36192436:Lancy132906@sql207.infinityfree.com/if0_36192436_domain_registration"
# SQLALCHEMY_DATABASE_URL =f'mssql+pyodbc://{user}:{password}@{server}/{db_name}?driver=ODBC Driver 17 for SQL Server'


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
