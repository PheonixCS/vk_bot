from repository.BaseModel import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class User(Base):
    __tablename__ = 'users'

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    login = mapped_column(String, nullable=False)  # добавить nullable
    password = mapped_column(String, nullable=False)  # добавить nullable
    group_id = mapped_column(Integer, ForeignKey("groups.id"), nullable=True)  # Добавление внешнего ключа
    group = relationship("Group", back_populates="users")

    async def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"


class Group(Base):
    __tablename__ = 'groups'
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String, nullable=False)  # добавить nullable
    users = relationship("User", back_populates="group")