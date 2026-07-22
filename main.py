from login import login
from booking import book_ticket
from ticket import view_ticket
from cancel import cancel_ticket
if login():
    while True:
        print("\n===== Ticket Booking System =====")
        print("1. Book Ticket")
        print("2. View Ticket")
        print("3. Cancel Ticket")
        print("4. Exit")
        choice = input("Enter Choice: ")
        if choice == "1":
            book_ticket()
        elif choice == "2":
            view_ticket()
        elif choice == "3":
            cancel_ticket()
        elif choice == "4":
            print("Thank You")
            break
        else:
            print("Invalid Choice")