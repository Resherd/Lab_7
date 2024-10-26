import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='userl',
    password='userp',
    database='pharmacy'
)

cursor = connection.cursor()

# Створення таблиці Medicine
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Medicine (
        registration_number INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        manufacture_date DATE NOT NULL,
        shelf_life_days INT NOT NULL,
        group_name VARCHAR(50) NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        prescription_required BOOLEAN NOT NULL
    );
""")

# Створення таблиці Suppliers
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Suppliers (
        supplier_code INT AUTO_INCREMENT PRIMARY KEY,
        supplier_name VARCHAR(255) NOT NULL,
        address VARCHAR(255) NOT NULL,
        phone VARCHAR(15) NOT NULL,
        contact_person VARCHAR(255),
        location ENUM('Ukraine', 'Other Country') NOT NULL
    );
""")

# Створення таблиці Deliveries
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Deliveries (
        delivery_code INT AUTO_INCREMENT PRIMARY KEY,
        delivery_date DATE NOT NULL,
        medicine_registration_number INT,
        quantity INT NOT NULL,
        supplier_code INT,
        FOREIGN KEY (medicine_registration_number) REFERENCES Medicine(registration_number),
        FOREIGN KEY (supplier_code) REFERENCES Suppliers(supplier_code)
    );
""")

connection.commit()
cursor.close()
connection.close()

print("Таблиці успішно створено!")
