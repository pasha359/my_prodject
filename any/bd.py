from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String,ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
meta = MetaData()

user = 'pasha_1'
password = 'pasha'
db_name = 'pasha_1'
engine = create_engine(
    f'postgresql://{user}:{password}@localhost:5432/{db_name}'
)
meta.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Organization(Base):
    __tablename__ = 'organization'

    id_org = Column(Integer, primary_key=True)
    name = Column(String(250))
    # city = Column(String, ForeignKey('Adress.city'))
    # country = Column(String,ForeignKey('Adress.country'))
    # users = Column(Integer,ForeignKey('user_id'))

    def __repr__(self) -> str:
        return f'<organization {self.id_org} - {self.name}>'

class Adress(Base):
    __tablename__ = 'adress'

    city = Column(primary_key=True)
    country = Column(String(250))
    # organization = relationship('Organization')
    # profil = relationship('Profil')

    def __repr__(self) -> str:
        return f'<adress {self.country} - {self.city}>'

class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key= True)
    name = Column(String(250))
    # profil = relationship('Frofil')

    def __repr__(self) -> str:
        return f'<iser {self.user_id} - {self.name}>'

class Profil(Base):
    __tablename__ = 'profil'

    profil_id = Column(Integer, primary_key=True)
    profil_name = Column(String(250))
    profil_last_name = Column(String(250))
    profil_adress = Column(String(250))
    # city = Column(String, ForeignKey('Adress.city'))
    # counry = Column(String,ForeignKey('Adress.country'))
    # users = Column(String, ForeignKey('Users.user_id'))
    # Adress = relationship('Adress')
    # Users = relationship('Users')


    def __repr__(self) -> str:
        return f'<profil {self.profil_id} - {self.profil_name} {self.profil_last_name}, {self.city}>'


org = Organization(name = 'alfa')
session.add(org)
session.commit()

adres = Adress(city = 'minsk', country = 'Belarus')
session.add(adres)
session.commit()

frofil = Profil(profil_name = 'pasha',profil_last_name = 'Dep', profil_adress = 'Minsk')
session.add(frofil)
session.commit()

user = Users(name = 'Jingls')
session.add(user)
session.commit()
