from database import ticket
def cancel_ticket():
    if ticket:
        ticket["status"] = "Cancelled"
        print("Ticket Cancelled Successfully")
    else:
        print("No Ticket Found")