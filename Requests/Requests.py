import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="userl",
    password="userp",
    database="pharmacy"
)

def print_results(title, results):
    print(f"\n{title}:\n{'-' * len(title)}")
    for result in results:
        print(result, "\n" + "-" * 30)

cursor = connection.cursor()

# Відобразити всі ліки, що відпускаються за рецептом лікаря, відсортовані за назвою
cursor.execute("SELECT * FROM Medicine WHERE prescription_required = 1 ORDER BY name")
print_results("Ліки, які відпускаються за рецептом лікаря", cursor.fetchall())

# Відобразити всі ліки за обраною групою
group = 'Cardiovascular'  
cursor.execute("SELECT * FROM Medicine WHERE group_name = %s", (group,))
print_results(f"Ліки з групи {group}", cursor.fetchall())

# Порахувати вартість кожної поставки
cursor.execute("""
    SELECT d.delivery_date, d.medicine_registration_number, d.quantity, d.supplier_code, 
           d.quantity * m.price AS total_cost 
    FROM Deliveries d
    JOIN Medicine m ON d.medicine_registration_number = m.registration_number
""")
print_results("Вартість кожної поставки", cursor.fetchall())

# Порахувати загальну суму грошей, яку сплатила аптека кожному постачальнику
cursor.execute("""
    SELECT s.supplier_name, SUM(d.quantity * m.price) AS total_paid 
    FROM Deliveries d 
    JOIN Suppliers s ON d.supplier_code = s.supplier_code 
    JOIN Medicine m ON d.medicine_registration_number = m.registration_number
    GROUP BY s.supplier_name
""")
print_results("Загальна сума грошей, сплачена кожному постачальнику", cursor.fetchall())

# Кількість поставок для кожної групи ліків від вітчизняних та закордонних постачальників
cursor.execute("""
    SELECT m.group_name, 
           SUM(CASE WHEN s.location = 'Ukraine' THEN 1 ELSE 0 END) AS Domestic, 
           SUM(CASE WHEN s.location = 'Other Country' THEN 1 ELSE 0 END) AS International 
    FROM Deliveries d 
    JOIN Suppliers s ON d.supplier_code = s.supplier_code 
    JOIN Medicine m ON d.medicine_registration_number = m.registration_number 
    GROUP BY m.group_name
""")
print_results("Кількість поставок для кожної групи ліків", cursor.fetchall())

# Остання дата придатності для кожного ліки
cursor.execute("""
    SELECT name, MAX(DATE_ADD(manufacture_date, INTERVAL shelf_life_days DAY)) AS last_expiry_date 
    FROM Medicine 
    GROUP BY name
""")
print_results("Остання дата придатності для кожного ліки", cursor.fetchall())

cursor.close()
connection.close()
