from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    message = Column(Text)

    status = Column(String)  # hot / warm / cold
    summary = Column(Text)
    response = Column(Text)