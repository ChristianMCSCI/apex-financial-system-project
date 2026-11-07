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
            