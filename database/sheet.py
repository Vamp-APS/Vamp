from sqlalchemy import Column, Integer, String

from database.base import Base


class Sheet(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    clan = Column(Integer)
