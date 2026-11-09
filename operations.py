from apexdatabasesystem import get_database_connection
import pymysql

def add_category(category_name, category_type):
    """Inserts a new category into the database securely."""
    
    connection = get_database_connection()
    if connection is None:
        print("Cannot proceed: Database connection failed.")
        return False
        
    try:
        with connection.cursor() as cursor:
            # 2. Write the raw SQL using %s placeholders for the values
            # Hint: INSERT INTO table_name (column1, column2) VALUES (%s, %s)
            sql = "INSERT INTO categories (category_name, category_type) VALUES (%s, %s)"
            
            # 3. Execute the cursor, passing the sql and a tuple of the variables
            cursor.execute(sql, (category_name, category_type))
            
        # 4. Commit the transaction so it saves to the disk!
        connection.commit()
        print(f"Success: Category '{category_name}' added to the ledger.")
        return True

    except pymysql.MySQLError as e:
        print(f"Database Error while adding category: {e}")
        return False
        
    finally:
        # 5. Always close the connection to prevent memory leaks
        connection.close()
        
        
def add_transaction(transaction_date, amount, category_id, description):
    
    connection = get_database_connection()
    if connection is None:
        print("Cannot proceed: Database connection failed.")
        return False
    
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO transactions (transaction_date, transaction_description, transaction_amount, category_id) VALUES (%s, %s, %s, %s)"
            
            cursor.execute(sql, (transaction_date, description, amount, category_id))
            
        connection.commit()
        print(f"Success: Transaction of ${amount} added to the ledger.")
        return True

    except pymysql.MySQLError as e:
        print(f"Database Error while adding transaction: {e}")
        return False

    finally:
        connection.close()
            
            
def view_categories():
    """Retrieves and prints all categories from the database."""
    connection = get_database_connection()
    if connection is None:
        print("Cannot proceed: Database connection failed.")
        return False
        
    try:
        with connection.cursor() as cursor:

            sql = "SELECT category_id, category_name, category_type FROM categories"
            
            cursor.execute(sql)
            
            categories = cursor.fetchall()
            
            for category in categories:
                print(f"ID: {category[0]}, Name: {category[1]}, Type: {category[2]}")
            
            return True

    except pymysql.MySQLError as e:
        print(f"Database Error while retrieving categories: {e}")
        return False
        
    finally:
        connection.close()
        
def view_all_transactions():
    """Retrieves and prints all transactions, joined with their category names."""
    connection = get_database_connection()
    if connection is None:
        print("Cannot proceed: Database connection failed.")
        return False
        
    try:
        with connection.cursor() as cursor:
            # TODO 5: Write the SQL SELECT query. 
            # Requirement: You must use an INNER JOIN to connect the 'transactions' 
            # table and the 'categories' table so you can display the category_name.
            sql = "SELECT transaction_date, transaction_id, transaction_description, transaction_amount, category_name FROM transactions INNER JOIN categories ON transactions.category_id = category_id"
            
            # TODO 6: Execute the query
            cursor.execute(sql)
            # TODO 7: Fetch all results
            transactions = cursor.fetchall()
            
            # TODO 8: Loop through 'transactions' and print them clearly
            for transaction in transactions:
                print(f"Date: {transaction[0]}, ID: {transaction[1]}, Description: {transaction[2]}, Amount: {transaction[3]}, Category: {transaction[4]} ")

    except pymysql.MySQLError as e:
        print(f"Database Error while retrieving transactions: {e}")
        return False
        
    finally:
        connection.close()