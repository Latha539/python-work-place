# Collecting user input
movie_name = input("Enter the movie name: ")
theater_name = input("Enter the theater name: ")
customer_name = input("Enter your name: ")
ticket_price = float(input("Enter ticket price ($): "))
num_tickets = int(input("Enter number of tickets: "))
show_time = input("Enter the show time (e.g., 7:30 PM): ")

# Calculating total cost
total_cost = ticket_price * num_tickets

# Displaying info using different string formatting methods

print("\n----- Ticket Summary Using Different Formatting Styles -----\n")

# 1. Comma-separated values (for basic printing)
print("Movie Name:", movie_name, "| Theater:", theater_name, "| Time:", show_time)

# 2. Percentage formatting
print("Customer: %s | Tickets: %d | Price per ticket: $%.2f" % (customer_name, num_tickets, ticket_price))

# 3. .format() method
print("Total cost using .format(): ${:.2f}".format(total_cost))

# 4. f-string formatting (introduced in Python 3.6)
print(f"Thank you, {customer_name}, for booking {num_tickets} ticket(s) to '{movie_name}' at {show_time}.")
print(f"Your total payment of ${total_cost:.2f} has been processed.")






