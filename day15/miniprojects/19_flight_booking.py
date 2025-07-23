# 19. Flight Booking Simulation

# Use Case: Book tickets for passengers with constraints. 
# Exception Handling Goals:
# Raise NoSeatsAvailableError
# Catch user errors (invalid ID, date)
# Use custom exceptions for frequent flyers
# Always log status with finally

import logging
from datetime import datetime

# Setup logging
logging.basicConfig(filename="flight_booking.log", level=logging.INFO, format='%(asctime)s - %(message)s')

# Custom Exceptions
class NoSeatsAvailableError(Exception):
    pass

class FrequentFlyerError(Exception):
    pass

def book_flight():
    total_seats = 5
    booked_seats = 0
    frequent_flyers = {"FF123", "FF456"}

    try:
        passenger_id = input("Enter Passenger ID: ").strip()
        booking_date_str = input("Enter booking date (YYYY-MM-DD): ").strip()

        if not passenger_id:
            raise ValueError("Passenger ID cannot be empty.")

        # Validate date format
        try:
            booking_date = datetime.strptime(booking_date_str, "%Y-%m-%d")
            if booking_date < datetime.now():
                raise ValueError("Booking date cannot be in the past.")
        except ValueError as ve:
            raise ValueError(f"Invalid date: {ve}")

        if passenger_id in frequent_flyers:
            raise FrequentFlyerError(f"Passenger {passenger_id} is a frequent flyer - special booking process.")

        if booked_seats >= total_seats:
            raise NoSeatsAvailableError("No seats available for this flight.")

        # Simulate booking success
        booked_seats += 1
        print(f"✅ Booking successful for {passenger_id} on {booking_date_str}.")

    except FrequentFlyerError as ffe:
        logging.warning(str(ffe))
        print(f"⚠️ {ffe} Contact support for assistance.")
    except NoSeatsAvailableError as nsae:
        logging.error(str(nsae))
        print(f"❌ {nsae}")
    except ValueError as ve:
        logging.error(str(ve))
        print(f"❌ Input Error: {ve}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}", exc_info=True)
        print(f"❌ Unexpected error: {e}")
    finally:
        logging.info(f"Booking attempt by Passenger ID: {passenger_id}, Date: {booking_date_str}")

if __name__ == "__main__":
    book_flight()
