import datetime

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Medidas(Base):
    __tablename__ = 'medidas'
    id = Column(Integer, primary_key=True)
    ultrasonido = Column('ultrasonido', Integer)
    servomotor = Column('servomotor', Integer)
    potenciometro = Column('potenciometro', Integer)

"""def serialize(self):
    return{'id' : self.id,
    'ultrasonido' : self.ultrasonido,
    'servomotor' : self.servomotor,
    'potenciometro' : self.potenciometro
    }"""
