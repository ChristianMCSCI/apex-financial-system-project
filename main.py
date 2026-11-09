from operations import add_category, add_transaction, view_categories, view_all_transactions

def main_menu():
    """Displays the main menu and handles user routing."""
    print("\n--- Apex Financial Ledger ---")
    
    while True:
        print("\nMain Menu:")
        print("1. View All Categories")
        print("2. Add a New Category")
        print("3. View All Transactions")
        print("4. Add a New Transaction")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
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
            transaction_amount = float(input("Enter amount (e.g., 50.00): "))
            category_id = int(input("Enter the Category ID: "))
            transaction_description = input("Enter a brief description: ")
            add_transaction(transaction_date, transaction_amount, category_id, transaction_description)
            
        elif choice == '5':
            print("Exiting Apex Financial Ledger. Goodbye!")
            break
            
        else:
            print("Invalid selection. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main_menu()