# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, DeclarativeBase
# from sqlalchemy.ext.declarative import declarative_base
# from app.backend.base import Base
# from sqlalchemy.schema import CreateTable
# from app.models.user import User
# from app.models.task import Task
#
# engine = create_engine('sqlite:///taskmanager.db', echo=True)
#
# SessionLocal = sessionmaker(bind=engine)
#
# # class Base(DeclarativeBase):
# #     pass
#
# # Base = declarative_base()
#
# from sqlalchemy.schema import CreateTable
# from app.backend.db import engine
#
# # Создаем таблицу для пользователей
# print(CreateTable(User.__table__).compile(engine))
#
# # Создаем таблицу для задач
# print(CreateTable(Task.__table__).compile(engine))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.backend.base import Base

engine = create_engine('sqlite:///taskmanager.db', echo=True)
SessionLocal = sessionmaker(bind=engine)

def create_tables():
    from app.models.user import User  # Импортируйте модели только внутри функции
    from app.models.task import Task
    # Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    create_tables()