import sqlite3
# you will need to pip install pandas matplotlib
import pandas as pd
import matplotlib as mpl

def get_connection(db_path="orders.db"):
    """
    Establish a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

# List all product categories
def product_categories(conn):
    query = "SELECT DISTINCT(category) FROM products;"
    cursor = conn.execute(query)

    print(f"Product Categories:")
    for category in cursor:
        print(f" - {category}")

# Count total number of customers
def total_customers(conn):
    query = "SELECT COUNT(*) FROM customers;"
    cursor = conn.execute(query)
    total_customers = cursor.fetchone()

    if total_customers:
        print(f"Total Customers: {total_customers}")

# Show all orders for a given customer (asks for a specific email)
def customer_orders(conn):
    data = {
        "order_id": [],
        "customer_id": [],
        "order_date": [],
        "status": [],
        "total_amount": []
    }

    email = input("Input email: ")
    query = '''
            SELECT O.orders FROM customers C
            LEFT JOIN orders O ON C.customer_id = O.customer_id
            WHERE email = ?;
            '''
    cursor = conn.execute(query, (email,))

    for each in cursor:
        data["order_id"].append(each[0])
        data["customer_id"].append(each[1])
        data["order_date"].append(each[2])
        data["status"].append(each[3])
        data["total_amount"].append(each[4])

    df = pd.DataFrame(data)
    print(df)
        

def main():

    db = get_connection()

    db.close()


if __name__=="__main__":
    main()
