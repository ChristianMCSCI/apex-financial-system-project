from operations import add_category, add_transaction, view_categories, view_all_transactions, update_transaction, delete_transaction, view_total_balance, view_spending_by_category

def get_valid_float(prompt_text):
    """Safely gets a float input from the user without crashing."""
    while True:
        user_input = input(prompt_text)
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input: Please enter a valid numerical amount (e.g., 50.00).")

def get_valid_int(prompt_text):
    """Safely gets an integer input from the user without crashing."""
    while True:
        user_input = input(prompt_text)
        try:
            return int(user_input)
        except ValueError:
            print("Invalid Input: please enter a valid whole number.")

def main_menu():
    """Displays the main menu and handles user routing."""
    print("\n--- Apex Financial Ledger ---")
    
    while True:
        print("\nMain Menu:")
        print("1. View All Categories")
        print("2. Add a New Category")
        print("3. View All Transactions")
        print("4. Add a New Transaction")
        print("5. Update a Transaction")
        print("6 Delete a Transaction")
        print("7. View Total Balance")
        print("8. View Total Spending By Category")
        print("9. Exit")
        
        choice = input("Select an option (1-9): ")
        
        if choice == '1':
            print("\n-- Categories --")
            view_categories()
            
        elif choice == '2':
            print("\n-- Add Category --")
            name = input("Enter category name (e.g., Rent, Groceries): ")
            category_type = input("Enter category type ('Income' or 'Expense'): ")
            add_category(name, category_type)
            
        elif choice == '3':
            print("\n-- Transactions --")
            view_all_transactions()
            
            
        elif choice == '4':
            print("\n-- Add Transaction --")
            transaction_date = input("Enter date (YYYY-MM-DD): ")
            transaction_amount = get_valid_float("Enter amount (e.g., 50.00): ")
            category_id = get_valid_int("Enter the Category ID: ")
            transaction_description = input("Enter a brief description: ")
            add_transaction(transaction_date, transaction_amount, category_id, transaction_description)
        
        elif choice == '5':
            print("\n-- Update Transaction --")
            transaction_id = get_valid_int("Enter the ID of the transaction to update: ")
            new_amount = get_valid_float("Enter the new amount: ")
            new_description = input("Enter the new description: ")
            update_transaction(transaction_id, new_amount, new_description)            
        elif choice == '6':
            print("\n-- Delete Transaction --")
            transaction_id = get_valid_int("Enter the ID of the transaction to delete: ")
            delete_transaction(transaction_id)
        
        elif choice == '7':
            print("\n-- Total Balance --")
            view_total_balance()
            
        elif choice == '8':
            print("\n-- Category Spending --")
            view_spending_by_category()
                
        elif choice == '9':
            print("Exiting Apex Financial Ledger. Goodbye!")
            break
            
        else:
            print("Invalid selection. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main_menu()