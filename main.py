# Railway Reservation System
print("Welcome to Railway Reservation System")
seats = 50
bookings = {}

def check_availability():
    print("Available seats:", seats)

def book_ticket():
    global seats
    if seats <= 0:
        print("No seats available!")
        return
    
    name = input("Enter name: ")
    age = input("Enter age: ")
    
    booking_id = len(bookings) + 1
    bookings[booking_id] = {"name": name, "age": age}
    
    seats -= 1
    print("Ticket booked successfully!")
    print("Your Booking ID:", booking_id)

def view_ticket():
    booking_id = int(input("Enter booking ID: "))
    
    if booking_id in bookings:
        print("Name:", bookings[booking_id]["name"])
        print("Age:", bookings[booking_id]["age"])
    else:
        print("Booking not found!")

def cancel_ticket():
    global seats
    booking_id = int(input("Enter booking ID to cancel: "))
    
    if booking_id in bookings:
        del bookings[booking_id]
        seats += 1
        print("Ticket cancelled successfully!")
    else:
        print("Booking not found!")

while True:
    print("\n--- Railway Reservation System ---")
    print("1. Check Availability")
    print("2. Book Ticket")
    print("3. View Ticket")
    print("4. Cancel Ticket")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        check_availability()
    elif choice == "2":
        book_ticket()
    elif choice == "3":
        view_ticket()
    elif choice == "4":
        cancel_ticket()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
