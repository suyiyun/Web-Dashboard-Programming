from sqlalchemy import create_engine
froms qlalchemy.ext.declarative import declarative_base
froms qlalchemy.orm import sessionmake

SQLALCHEMY_DATABASE_URL = "postgresql://pguser:pgpass@postgresql:5432/pgdb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base=declarative_base()
