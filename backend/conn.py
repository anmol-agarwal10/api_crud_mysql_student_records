import mysql.connector as mysql

class DatabaseConnection:
    def __init__(self):

    # Initialize the database connection
        self.conn = mysql.connect(
            host="localhost",
            user="root",
            password="12345",
            database="studentdb"
        )
        self.cursor = self.conn.cursor()    

    # Method to execute read queries
    def read(self, query):
        self.cursor.execute("use studentdb")
        self.cursor.execute(query)
        details = self.cursor.fetchall()
        return details
    
    # Method to execute write queries
    def write(self, query):
        self.cursor.execute("use studentdb")
        self.cursor.execute(query)
        self.conn.commit()
