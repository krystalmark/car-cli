from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///car_database.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    zip_code = Column(String)  # Add zip code column
    state = Column(String)  # Add state column
    city = Column(String)  # Add city column
    cars = relationship('Car', back_populates='owner')

class Car(Base):
    __tablename__ = 'cars'
    
    id = Column(Integer, primary_key=True)
    brand = Column(String(255), nullable=False)
    model = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    serial_number = Column(String(10), unique=True, nullable=False)
    stolen = Column(Boolean, default=False)
    city = Column(String)
    state = Column(String)  # Add state column
    zip_code = Column(String)  # Add zip code column

    
    user_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='cars')
    
    stolen_report = relationship('StolenCar', uselist=False, back_populates='car')

class StolenCar(Base):
    __tablename__ = 'stolen_cars'
    
    id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey('cars.id'))
    
    car = relationship('Car', back_populates='stolen_report')

engine = create_engine('sqlite:///car_database.db')
Base.metadata.create_all(engine)
