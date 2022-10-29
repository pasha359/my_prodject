from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from settings_acces import user_db,password_db,name_db

engine = create_engine(
    f'postgresql://{user_db}:{password_db}@localhost:5432/{name_db}')

Base = declarative_base()

class Telebot(Base):
    __tablename__ = 'telebot'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    date = Column(DateTime, default=datetime.now())


Session = sessionmaker(bind=engine)
session = Session()


def save_user(name):
    user_list = []
    for single_name in session.query(Telebot.name):
        user_list.append(single_name.name)
    if name not in user_list:
        user = Telebot(name=name)
        session.add(user)
        session.commit()
        print(f'{name} is saved')