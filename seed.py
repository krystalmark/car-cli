from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Car, StolenCar
from faker import Faker

engine = create_engine('sqlite:///car_database.db')
Session = sessionmaker(bind=engine)
session = Session()
fake = Faker()

# Generate fake user data
users_data = [
    {
        'name': fake.name(),
        'email': fake.email(),
        'zip_code': fake.zipcode(),
        'state': fake.state_abbr(),
        'city': fake.city()
    } for _ in range(67)
]

# Add users to the session
for user_data in users_data:
    user = User(
        name=user_data['name'],
        email=user_data['email'],
        zip_code=user_data['zip_code'],
        state=user_data['state'],
        city=user_data['city']
    )
    session.add(user)

# Generate fake car data
cars_data = [
    {
        'brand': fake.company(), 
        'model': fake.random_element(elements=('Sedan', 'SUV', 'Truck')),
        'year': fake.random_int(min=2000, max=2023), 
        'serial_number': fake.unique.random_number(digits=10),
        'user_id': fake.random_int(min=1, max=67)
    } for _ in range(67)
]

# Add cars to the session
for car_data in cars_data:
    car = Car(
        brand=car_data['brand'], 
        model=car_data['model'], 
        year=car_data['year'],
        serial_number=car_data['serial_number'], 
        user_id=car_data['user_id']
    )
    session.add(car)

# Generate fake stolen car data
stolen_cars_data = [
    {'car_id': fake.random_int(min=1, max=67)} for _ in range(67)
]

# Add stolen cars to the session
for stolen_car_data in stolen_cars_data:
    stolen_car = StolenCar(car_id=stolen_car_data['car_id'])
    session.add(stolen_car)

# Commit the changes
session.commit()
