cities = {
    "Hyderabad": 500,
    "Bangalore": 700,
    "Chennai": 600,
    "Mumbai": 1200,
    "Delhi": 1500,
    "Kolkata": 1000,
    "Pune": 800
}
def show_destinations():
    print("\nAvailable Destinations")
    for city, price in cities.items():
        print(f"{city} - ₹{price}")