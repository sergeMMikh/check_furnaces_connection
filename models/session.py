from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DSN = 'postgresql://smm:vrag@localhost:5432/furnace_history'

engine = create_engine(DSN)
Base = declarative_base()
Session = sessionmaker(bind=engine)
