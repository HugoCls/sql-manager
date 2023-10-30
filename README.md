# sql-manager

The `sql-manager` module provides a simple database class intended to simplify the use of the `mysql-connector-python` module for working with MySQL databases.

## Installation
 
1. Make sure you have the `mysql-connector-python` module installed. If not, use `pip`:
```
pip install mysql-connector-python
```

  
2. Download or clone the `sql-manager` repository:
```
git clone https://github.com/HugoCls/sql-manager.git
```
3. Import the `Database` class into your Python code to use it:

```python
from Database_class import Database
```
## Usage
### Initialization

To start using sql-manager, create an instance of the Database class by specifying the connection parameters for your database:

```python
database = Database(
	host="your_host",
	port="your_port",
	user="your_user",
	password="your_password",
	database="your_database",
)
```
## Creating/Deleting Tables
```python
database.create_tables()

database.delete_table("table_name")
```
## Retrieving Data
To fetch data from a table and get it as a DataFrame, you can either use ```get_table``` to get the whole table:

```python
dataframe = database.get_table("table_name")
```

Or use ```custom_select_query```:

```python
query="""
SELECT
	*
FROM [table_name]
WHERE [condition]
"""
dataframe = database.custom_select_query(query, "table_name")
```

## Executing a custom query with no result
```python
database.custom_query("YOUR_SQL_QUERY")
```
Exemple of usage: INSERT queries

## Database Backup
The save_database method allows you to save your database to an SQL file. Specific tables to save are configured in the save_database method through the tables variable (in the example above, the "Priceslogs" table is saved).

```python
database.save_database()
```
Here is an exemple of ```backup.sql``` file:
```sql
--- Table: Books
CREATE TABLE IF NOT EXISTS Books (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(255),
    Author VARCHAR(255),
    PublishedYear INT,
    Price DECIMAL(10, 2)
);

INSERT INTO Books VALUES (1, 'The Great Gatsby', 'F. Scott Fitzgerald', 1925, 12.99);
INSERT INTO Books VALUES (2, 'To Kill a Mockingbird', 'Harper Lee', 1960, 14.95);
INSERT INTO Books VALUES (3, '1984', 'George Orwell', 1949, 9.99);
```
Query this file gets you your database setup instantly.
