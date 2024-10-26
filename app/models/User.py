from repository.BaseModel import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class User(Base):
    __tablename__ = "users" 
    id = Column(Integer, primary_key=True)
    login = Column(String)   
    hash_password = Column(String)
    role = Column(String)
    #groups = Column(Integer, ForeignKey('group.id'))