# apex-financial-system-project
# Apex Financial Ledger

A robust, command-line interface (CLI) financial ledger application built with Python and MySQL. This application allows users to track income and expenses, manage financial categories, and generate real-time financial reporting.

## Features
- **Full CRUD Operations**: Create, Read, Update, and Delete financial transactions.
- **Categorization**: Group transactions by custom Income or Expense categories.
- **Financial Analytics**: Generate real-time reports calculating net balance and total spending by category.
- **Data Security**: Environment variable management using `python-dotenv` to keep database credentials out of the source code.
- **Resilient UI**: Built-in error handling and input validation prevents application crashes from invalid user data entry.

## Tech Stack
- **Language**: Python 3.x
- **Database**: MySQL
- **Libraries**: `PyMySQL` (Database connection), `python-dotenv` (Environment management)

## Installation & Setup

### 1. Clone the repository
`git clone (https://github.com/ChristianMCSCI/apex-financial-system-project)`
`cd your-repo-name`

### 2. Install dependencies
`pip install pymysql python-dotenv`

### 3. Database Configuration
1. Open MySQL and execute the `apexfinancialsystemsetup.sql` script to build the `apexfinancialdb` schema.
2. Create a `.env` file in the root directory of this project.
3. Add your database credentials to the `.env` file exactly like this (no quotes or spaces):
`DB_HOST=localhost`
`DB_USER=root`
`DB_PASSWORD=your_mysql_password`
`DB_NAME=apexfinancialdb`

### 4. Run the Application
Start the CLI application by running the main Python script:
`python main.py`

## Project Structure
- `main.py`: The entry point for the application. Contains the CLI loop, routing, and user input validation.
- `operations.py`: The backend engine containing all parameterized SQL queries (CRUD and Aggregations).
- `apexdatabasesystem.py`: Handles the secure connection bridge between Python and MySQL using environment variables.
