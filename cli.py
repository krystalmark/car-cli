
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Car  

DB_URL = "sqlite:///car_database.db"

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass

@cli.command()
def display():
    user_id = click.prompt("Enter user ID", type=int)
    user = session.query(User).filter_by(id=user_id).first()

    if user:
        cars = user.cars
        if cars:
            click.echo(f"Cars for User ID {user_id}:")
            for car in cars:
                click.echo(f"Car ID: {car.id}, Brand: {car.brand}, Model: {car.model}, Year: {car.year}, Serial Number: {car.serial_number}")
        else:
            click.echo(f"No cars found for User ID {user_id}")
    else:
        click.echo(f"User with ID {user_id} not found in the database.")

@cli.command()
def remove():
    car_id = click.prompt("Enter car ID to remove", type=int)
    car = session.query(Car).filter_by(id=car_id).first()

    if car:
        session.delete(car)
        session.commit()
        click.echo(f"Car with ID {car_id} has been removed from the database.")
    else:
        click.echo(f"Car with ID {car_id} not found in the database.")

@cli.command()
def update():
    car_id = click.prompt("Enter car ID to update", type=int)
    field = click.prompt("Enter field to modify", type=click.Choice(["brand", "model", "year", "serial_number"]))
    new_value = click.prompt("Enter new value")

    car = session.query(Car).filter_by(id=car_id).first()

    if car:
        setattr(car, field, new_value)
        session.commit()
        click.echo(f"Car with ID {car_id} has been updated.")
    else:
        click.echo(f"Car with ID {car_id} not found in the database.")

@cli.command()
def report():
    car_id = click.prompt("Enter car ID to report as stolen", type=int)
    car = session.query(Car).filter_by(id=car_id).first()

    if car:
        car.stolen = True
        session.commit()
        click.echo(f"Car with ID {car_id} has been reported as stolen.")
    else:
        click.echo(f"Car with ID {car_id} not found in the database.")

@cli.command()
def search():
    city = click.prompt("Enter city to search in")
    state = click.prompt("Enter state to search in")
    zip_code = click.prompt("Enter zip code to search in")

    cars = session.query(Car).filter_by(stolen=True, city=city, state=state, zip_code=zip_code).all()

    if cars:
        click.echo("Stolen cars matching the search criteria:")
        for car in cars:
            click.echo(f"Car ID: {car.id}, Brand: {car.brand}, Model: {car.model}, Year: {car.year}, Serial Number: {car.serial_number}")
    else:
        click.echo("No stolen cars found matching the search criteria.")

if __name__ == "__main__":
    cli()
