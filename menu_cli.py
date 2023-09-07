import click
from models import User, Car, StolenCar, Session

Session = Session()

def display_menu():
    click.echo("Select an action:")
    click.echo("1. Display User's Cars")
    click.echo("2. Remove a Car")
    click.echo("3. Update Car Information")
    click.echo("4. Report a Car as Stolen")
    click.echo("5. Search for Cars")
    click.echo("6. Quit")

def display_users_cars():
    user_id = click.prompt("Enter user ID", type=int)

    user = Session.query(User).filter_by(id=user_id).first()

    if user:
        cars = user.cars
        if cars:
            click.echo(f"Cars for User ID: {user_id}")
            for car in cars:
                click.echo(f"Car ID: {car.id}, Brand: {car.brand}, Model: {car.model}, Year: {car.year}")
        else:
            click.echo(f"No cars found for User ID: {user_id}")
    else:
        click.echo(f"User with ID {user_id} not found in the database.")

def remove_car():
    car_id = click.prompt("Enter the ID of the car to remove", type=int)
    car = Session.query(Car).filter_by(id=car_id).first()

    if car:
        Session.delete(car)
        Session.commit()
        click.echo(f"Car with ID {car_id} has been removed from the database.")
    else:
        click.echo(f"Car with ID {car_id} not found in the database.")

def update_car():
    car_id = click.prompt("Enter car ID to update", type=int)
    field = click.prompt("Enter field to modify (brand, model, year, serial_number)")
    new_value = click.prompt("Enter new value for the field")

    car = Session.query(Car).filter_by(id=car_id).first()

    if car:
        if hasattr(car, field):
            setattr(car, field, new_value)
            Session.commit()
            click.echo(f"Car with ID {car_id} updated successfully.")
        else:
            click.echo(f"Invalid field: {field}")
    else:
        click.echo(f"Car with ID {car_id} not found in the database.")

def report_stolen():
    car_id = click.prompt("Enter car ID to report as stolen", type=int)

    car = Session.query(Car).filter_by(id=car_id).first()

    if car:
        car.stolen = True
        Session.commit()
        click.echo(f"Car with ID {car_id} reported as stolen.")
    else:
        click.echo(f"Car with ID {car_id} not found in the database.")

def search_cars():
    city = click.prompt("Enter city to search in")
    state = click.prompt("Enter state to search in")
    zip_code = click.prompt("Enter zip code to search in")

    cars = Session.query(Car).filter_by(city=city, state=state, zip_code=zip_code).all()

    if cars:
        click.echo(f"Search results for City: {city}, State: {state}, Zip Code: {zip_code}")
        for car in cars:
            click.echo(f"Car ID: {car.id}, Brand: {car.brand}, Model: {car.model}, Year: {car.year}")
    else:
        click.echo("No cars found matching the search criteria.")

@click.command()
def main():
    while True:
        display_menu()
        choice = click.prompt("Enter your choice", type=int)

        if choice == 1:
            display_users_cars()
        elif choice == 2:
            remove_car()
        elif choice == 3:
            update_car()
        elif choice == 4:
            report_stolen()
        elif choice == 5:
            search_cars()
        elif choice == 6:
            click.echo("Exiting...")
            break
        else:
            click.echo("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
