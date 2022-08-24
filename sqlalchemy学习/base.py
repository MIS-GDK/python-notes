from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "postgresql://aiohttpdemo_user:aiohttpdemo_pass@localhost:5432/aiohttpdemo_polls"
)
Session = sessionmaker(bind=engine)

Base = declarative_base()
