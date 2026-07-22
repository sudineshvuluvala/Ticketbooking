from destinations import cities, show_destinations
from payment import payment
from database import ticket
def book_ticket():
    show_destinations()
    name = input("\nPassenger Name: ")
    city = input("Destination: ")
    if city in cities:
        amount = cities[city]
        if payment(amount):
            ticket["name"] = name
            ticket["city"] = city
            ticket["price"] = amount
            ticket["status"] = "Booked"
            print("Ticket Booked Successfully")
    else:
        print("Invalid Destination")