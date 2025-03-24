import os
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


if not os.path.exists('data'):
    os.makedirs('data')


Base = declarative_base()
ruta_base_datos = os.path.abspath('data/empleados.db')  # Ruta absoluta
engine = create_engine(f'sqlite:///{ruta_base_datos}')
Session = sessionmaker(bind=engine)
session = Session()

class Empleado(Base):

    __tablename__ = 'empleados'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    salario = Column(Float, nullable=False)
    departamento = Column(String, nullable=False)

Base.metadata.create_all(engine)
