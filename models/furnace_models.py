from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy import ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class FurnaceIO(Base):
    __tablename__ = "furnace"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    ip = Column(String(12), unique=True, nullable=False)
    port = Column(String(6), unique=False, nullable=False)
    is_under_surveillance = Column(Boolean)


class FurnaceHistory(Base):
    __tablename__ = "measurements"
    id = Column(Integer, primary_key=True)
    furnace_id = Column(Integer, ForeignKey("furnace.id", ondelete="CASCADE"))
    temperature = Column(Integer)
    sp = Column(Integer)
    measured_at = Column(DateTime, server_default=func.now())
