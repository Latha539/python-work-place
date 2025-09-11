# movie_base.py
# Base Program: Defines all classes for Movie Ticket Booking System

import uuid

# Base Class
class Person:
    def __init__(self, name, email):
        self._name = name      # encapsulation
        self._email = email

    def display_info(self):
        raise NotImplementedError("Subclass must implement this method")


# Subclass: Customer
class Customer(Person):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.customer_id = str(uuid.uuid4())[:8]
        self.bookings = []

    def book_ticket(self, booking):
        self.bookings.append(booking)

    def view_bookings(self):
        for b in self.bookings:
            print(b.display_booking())

    def display_info(self):
        return f"Customer: {self._name}, Email: {self._email}, ID: {self.customer_id}"


# Subclass: Staff
class Staff(Person):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.staff_id = str(uuid.uuid4())[:8]
        self.role = role

    def display_info(self):
        return f"Staff: {self._name}, Role: {self.role}, ID: {self.staff_id}"


# Movie Class
class Movie:
    def __init__(self, title, genre, duration, rating):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating

    def display_info(self):
        return f"{self.title} ({self.genre}) - {self.duration} mins, Rating: {self.rating}"


# Showtime Class
class Showtime:
    def __init__(self, movie, time, total_seats):
        self.movie = movie
        self.time = time
        self.total_seats = total_seats
        self.available_seats = total_seats

    def reserve_seat(self, seats):
        if seats <= self.available_seats:
            self.available_seats -= seats
            return True
        return False

    def release_seat(self, seats):
        self.available_seats += seats

    def display_info(self):
        return f"{self.movie.title} at {self.time} | Seats: {self.available_seats}/{self.total_seats}"


# Booking Class
class Booking:
    def __init__(self, customer, showtime, seats):
        self.booking_id = str(uuid.uuid4())[:8]
        self.customer = customer
        self.showtime = showtime
        self.seats = seats

    def display_booking(self):
        return f"BookingID: {self.booking_id} | {self.customer._name} booked {self.seats} seats for {self.showtime.movie.title} at {self.showtime.time}"


# Manager Class: Cinema
class Cinema:
    total_revenue = 0

    def __init__(self, name):
        self.name = name
        self.movies = []
        self.showtimes = []
        self.customers = []
        self.bookings = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def add_showtime(self, showtime):
        self.showtimes.append(showtime)

    def register_customer(self, customer):
        self.customers.append(customer)

    def make_booking(self, customer, showtime, seats, ticket_price=10):
        if showtime.reserve_seat(seats):
            booking = Booking(customer, showtime, seats)
            customer.book_ticket(booking)
            self.bookings.append(booking)
            Cinema.total_revenue += seats * ticket_price
            print("✅ Booking successful!")
        else:
            print("❌ Not enough seats available.")

    @classmethod
    def generate_report(cls):
        return f"Total Revenue: ${cls.total_revenue}"
