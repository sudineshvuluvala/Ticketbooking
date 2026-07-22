def payment(amount):
    print("\nTicket Price:", amount)
    pay = int(input("Enter Amount: ₹"))
    if pay == amount:
        print("Payment Successful")
        return True
    print("Payment Failed")
    return False