from database import ticket
def view_ticket():
    if ticket:
        print("\n------ Ticket ------")
        for key, value in ticket.items():
            print(key, ":", value)
    else:
        print("No Ticket Found")