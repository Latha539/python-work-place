# main.py
# Main Program: CLI for Movie Ticket Booking System

from movie_base import Movie, Showtime, Customer, Cinema

def main():
    cinema = Cinema("Star Cinema")

    # Add movies
    m1 = Movie("Inception", "Sci-Fi", 148, "PG-13")
    m2 = Movie("Avengers", "Action", 180, "PG-13")
    cinema.add_movie(m1)
    cinema.add_movie(m2)

    # Add showtimes
    s1 = Showtime(m1, "6:00 PM", 50)
    s2 = Showtime(m2, "9:00 PM", 60)
    cinema.add_showtime(s1)
    cinema.add_showtime(s2)

    # Register a customer
    cust1 = Customer("Alice", "alice@example.com")
    cinema.register_customer(cust1)

    # CLI menu
    while True:
        print("\n--- Movie Ticket Booking System ---")
        print("1. View Movies")
        print("2. View Showtimes")
        print("3. Book Ticket")
        print("4. View My Bookings")
        print("5. Generate Report")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            for m in cinema.movies:
                print(m.display_info())

        elif choice == "2":
            for s in cinema.showtimes:
                print(s.display_info())

        elif choice == "3":
            print("Available Showtimes:")
            for idx, s in enumerate(cinema.showtimes):
                print(f"{idx+1}. {s.display_info()}")
            sel = int(input("Select showtime: ")) - 1
            seats = int(input("How many seats? "))
            cinema.make_booking(cust1, cinema.showtimes[sel], seats)

        elif choice == "4":
            cust1.view_bookings()

        elif choice == "5":
            print(Cinema.generate_report())

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again!")


if __name__ == "__main__":
    main()
