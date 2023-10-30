import mysql.connector
import pandas as pd
from datetime import datetime

class Database():
    def __init__(self, host, port, user, password, database):

        self.connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
        )

        self.cursor = self.connection.cursor()

    def create_tables(self):
        ## This is an exemple of CREATE TABLE query, change it if needed
        create_table_query = """
        CREATE TABLE IF NOT EXISTS Priceslogs (
            ProcessingDate TIMESTAMP,
            Name VARCHAR(255),
            Size VARCHAR(255),
            Price VARCHAR(255),
        );
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def delete_table(self, table):
        query = f"""
        DROP TABLE {table}
        """
        self.cursor.execute(query)
        self.connection.commit()

    def get_table(self, table_name):
        
        self.cursor.execute(f"DESCRIBE {table_name}")
        columns = [column[0] for column in self.cursor.fetchall()]

        self.cursor.execute(f"SELECT * FROM {table_name}")
        rows = self.cursor.fetchall()

        df = pd.DataFrame(rows, columns=columns)
        
        return df
    
    def custom_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()
    
    def custom_select_query(self, query, table_name):
        
        self.cursor.execute(f"DESCRIBE {table_name}")
        columns = [column[0] for column in self.cursor.fetchall()]

        self.cursor.execute(query)
        self.connection.commit()

        rows = self.cursor.fetchall()

        df = pd.DataFrame(rows, columns=columns)
        
        return df
    
    def save_database(self):
        
        output_file = "data/backup.sql"

        with open(output_file, "w") as file:

            self.cursor.execute("SHOW TABLES")
            tables = self.cursor.fetchall()

            for table in tables:
                table_name = table[0]

                if table_name in ["Priceslogs"]:
                    file.write(f"--- Table: {table_name}\n")

                    self.cursor.execute(f"SHOW CREATE TABLE {table_name}")
                    create_table_query = self.cursor.fetchone()[1]

                    file.write(create_table_query + ";\n")

                    self.cursor.execute(f"SELECT * FROM {table_name}")
                    rows = self.cursor.fetchall()
                    
                    for row in rows:
                        insert_query = f"INSERT INTO {table_name} VALUES {row};\n"
                        file.write(insert_query)