import sqlite3

# ==================================================
# Section 1 – Summaries
# ==================================================

def total_customers(conn):
    query = "SELECT COUNT(customer_id) FROM customers;"
    cursor = conn.execute(query)
    total_customers = cursor.fetchone()

    if total_customers:
        print(f"Total Customers: {total_customers}")

def customer_signup_range(conn):
    query1 = "SELECT signup_date FROM customers ORDER BY signup_date ASC LIMIT 1;"
    query2 = "SELECT signup_date FROM customers ORDER BY signup_date DESC LIMIT 1;"
    cursor1 = conn.execute(query1)
    cursor2 = conn.execute(query2)
    earliest = cursor1.fetchone()
    latest = cursor2.fetchone()
    
    if earliest and latest:
        print(f"Earliest Sign Up Date: {earliest}")
        print(f"Latest Sign Up Date: {latest}")

def order_summary_stats(conn):
    query = "SELECT COUNT(order_id), AVG(order_total), MAX(order_total), MIN(order_total) FROM orders;"
    cursor = conn.execute(query)
    stats = cursor.fetchone()

    if stats:
        print(f"# of Orders: {stats[0]}")
        print(f"Average Order Total: {stats[1]}")
        print(f"Max. Order Total: {stats[2]}")
        print(f"Min. Order Total: {stats[3]}")

def driver_summary(conn):
    query1 = "SELECT COUNT(*) FROM drivers;"
    query2 = "SELECT DISTINCT(hire_date) FROM drivers;"
    cursor1 = conn.execute(query1)
    cursor2 = conn.execute(query2)
    num_drivers = cursor1.fetchone()

    if num_drivers:
        print(f"# of Drivers: {num_drivers}")
    
    print(f"Hire Dates")
    for date in cursor2:
        print(f"  {date}")

# ==================================================
# Section 2 – Key Statistics
# ==================================================

def orders_per_customer(conn):
    query = '''
            SELECT C.customer_name, COUNT(O.order_Id), SUM(O.order_total)
            FROM customers C LEFT JOIN orders O
            ON C.customer_id = O.customer_id
            GROUP BY C.customer_id;
            '''
    cursor = conn.execute(query)

    for each in cursor:
        print(f"Name: {each[0]}\t# of Orders: {each[1]}\tTotal Spent: {each[2]}")


def driver_workload(conn):
    query = '''
            SELECT DR.driver_name, COUNT(DL.delivery_id)
            FROM drivers DR LEFT JOIN deliveries DL
            ON DR.driver_id = DL.driver_id
            GROUP BY DR.driver_id;
            '''
    cursor = conn.execute(query)

    for each in cursor:
        print(f"Name: {each[0]}\t# of Deliveries: {each[1]}")


def delivery_lookup_by_id(conn, order_id):
    query = '''
            SELECT C.customer_name, O.order_total, DL.delivery_date, DR.driver_name
            FROM orders O
            JOIN customers C ON O.customer_id = C.customer_id
            JOIN deliveries DL ON O.order_id = DL.order_id
            JOIN drivers DR ON DL.driver_id = DR.driver_id
            WHERE O.order_id = ?;
            '''

    cursor = conn.execute(query, (order_id,))
    delivery = cursor.fetchone()

    if delivery:
        print(f"Customer Name: {delivery[0]}")
        print(f"Order Total: {delivery[1]}")
        print(f"Delivery Date: {delivery[2]}")
        print(f"Customer ID: {delivery[3]}")
    else:
        print("No such delivery found.")

# ==================================================
# Section 3 – Time-based Summaries
# ==================================================

def orders_per_date(conn):
    pass


def deliveries_per_date(conn):
    pass


def customer_signups_per_month(conn):
    pass


# ==================================================
# Section 4 – Performance and Rankings
# ==================================================

def top_customers_by_spend(conn, limit=5):
    pass


def rank_drivers_by_deliveries(conn):
    pass


def high_value_orders(conn, threshold):
    pass


# ==================================================
# Menus - You should not need to change any code below this point until the stretch tasks.
# ==================================================

def section_1_menu(conn):
    while True:
        print("\nSection 1 – Summaries")
        print("1. Total number of customers")
        print("2. Customer signup date range")
        print("3. Order summary statistics")
        print("4. Driver summary")
        print("0. Back to main menu")

        choice = input("Select an option: ")

        if choice == "1":
            total_customers(conn)
        elif choice == "2":
            customer_signup_range(conn)
        elif choice == "3":
            order_summary_stats(conn)
        elif choice == "4":
            driver_summary(conn)
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")


def section_2_menu(conn):
    while True:
        print("\nSection 2 – Key Statistics")
        print("1. Orders per customer")
        print("2. Driver workload")
        print("3. Order delivery overview")
        print("0. Back to main menu")

        choice = input("Select an option: ")

        if choice == "1":
            orders_per_customer(conn)
        elif choice == "2":
            driver_workload(conn)
        elif choice == "3":
            order_id = input("Enter order ID: ").strip()
            if not order_id.isdigit():
                print("Please enter a valid integer order ID.")
                continue
            delivery_lookup_by_id(conn, int(order_id))
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")


def section_3_menu(conn):
    while True:
        print("\nSection 3 – Time-based Summaries")
        print("1. Orders per date")
        print("2. Deliveries per date")
        print("3. Customer signups per month")
        print("0. Back to main menu")

        choice = input("Select an option: ")

        if choice == "1":
            orders_per_date(conn)
        elif choice == "2":
            deliveries_per_date(conn)
        elif choice == "3":
            customer_signups_per_month(conn)
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")


def section_4_menu(conn):
    while True:
        print("\nSection 4 – Performance and Rankings")
        print("1. Top 5 customers by total spend")
        print("2. Rank drivers by deliveries completed")
        print("3. High-value orders")
        print("0. Back to main menu")

        choice = input("Select an option: ")

        if choice == "1":
            top_customers_by_spend(conn)
        elif choice == "2":
            rank_drivers_by_deliveries(conn)
        elif choice == "3":
            try:
                threshold = float(input("Enter order value threshold (£): "))
                high_value_orders(conn, threshold)
            except:
                print("Please enter a valid numerical value.")
        elif choice == "0":
            break
        else:
            print("Invalid option. Please try again.")


def main_menu(conn):
    while True:
        print("\n=== Delivery Service Management Dashboard ===")
        print("1. Section 1 – Summaries")
        print("2. Section 2 – Key Statistics")
        print("3. Section 3 – Time-based Summaries")
        print("4. Section 4 – Performance and Rankings")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            section_1_menu(conn)
        elif choice == "2":
            section_2_menu(conn)
        elif choice == "3":
            section_3_menu(conn)
        elif choice == "4":
            section_4_menu(conn)
        elif choice == "0":
            print("Exiting dashboard.")
            break
        else:
            print("Invalid option. Please try again.")

def get_connection(db_path="food_delivery.db"):
    """
    Establish a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

if __name__ == "__main__":
    conn = get_connection()
    main_menu(conn)
    conn.close()