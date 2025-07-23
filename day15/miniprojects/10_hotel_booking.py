# 10. Hotel Booking System

# Use Case: Accept user input for date, guest count, etc. 
# Exception Handling Goals:
# Raise OverBookingError if guests > rooms
# Validate date format
# Use multiple except blocks
# Use assert to ensure valid dates

from datetime import datetime

# Custom Exception
class OverBookingError(Exception):
    pass

def hotel_booking_system():
    total_rooms = 5 

    try:
        date_str = input("Enter booking date (YYYY-MM-DD): ")
        guests = int(input("Enter number of guests: "))

        # Validate date format
        try:
            booking_date = datetime.strptime(date_str, "%Y-%m-%d")
            assert booking_date >= datetime.now(), "Booking date cannot be in the past."
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
        except AssertionError as ae:
            raise ValueError(str(ae))

        # Check booking capacity
        if guests > total_rooms:
            raise OverBookingError(f"Cannot book for {guests} guests. Only {total_rooms} rooms available.")

    except OverBookingError as obe:
        print(f"❌ Overbooking Error: {obe}")
    except ValueError as ve:
        print(f"❌ Value Error: {ve}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
    else:
        print(f"✅ Booking successful for {guests} guests on {booking_date.strftime('%Y-%m-%d')}")
    finally:
        print("📝 Booking process completed.")


if __name__ == "__main__":
    hotel_booking_system()
