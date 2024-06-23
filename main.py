import mysql.connector

# Replace these values with your actual MySQL database credentials
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'chen liconga',
    'database': 'mydb'
}

# Connect to MySQL
try:
    connection = mysql.connector.connect(**db_config)
    if connection.is_connected():
        print('Connected to MySQL database')
        cursor = connection.cursor()
        # Example query
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print('connected')
except mysql.connector.Error as e:
    print(f'Error connecting to MySQL: {e}')
finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print('MySQL connection closed')
