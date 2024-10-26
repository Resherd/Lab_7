import mysql.connector


connection = mysql.connector.connect(
    host='localhost',
    user='userl',
    password='userp', 
    database='pharmacy'
)

def print_results(title, results):
    print(f"\n{title}:\n{'-' * len(title)}")
    for result in results:
        print(result, "\n" + "-" * 30)

cursor = connection.cursor()

# Виведення даних з таблиці Medicine
print("Дані з таблиці Medicine:")
cursor.execute("SELECT * FROM Medicine;")
medicine_data = cursor.fetchall()
for row in medicine_data:
    print(row)

# Виведення даних з таблиці Suppliers
print("\nДані з таблиці Suppliers:")
cursor.execute("SELECT * FROM Suppliers;")
suppliers_data = cursor.fetchall()
for row in suppliers_data:
    print(row)

# Виведення даних з таблиці Deliveries
print("\nДані з таблиці Deliveries:")
cursor.execute("SELECT * FROM Deliveries;")
deliveries_data = cursor.fetchall()
for row in deliveries_data:
    print(row)

cursor.close()
connection.close()
