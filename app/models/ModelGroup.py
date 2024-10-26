from repository.BaseModel import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Group(Base): 
    __tablename__ = 'groups'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str]
    from models.AllModels import User
    users: Mapped[list["User"]] = relationship("User", back_populates="group")