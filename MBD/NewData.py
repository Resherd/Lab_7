import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='userl',
    password='userp',
    database='pharmacy'
)

cursor = connection.cursor()
medicine  = [
    ('Aspirin', '2024-01-10', 365, 'Anti-inflammatory', 120.50, True),
    ('Paracetamol', '2023-12-05', 730, 'Painkiller', 85.00, True),
    ('Ibuprofen', '2023-11-20', 540, 'Anti-inflammatory', 150.00, True),
    ('Vitamin C', '2024-03-15', 1095, 'Vitamins', 200.00, False),
    ('Amoxicillin', '2023-10-01', 730, 'Antibiotic', 95.00, True),
    ('Metformin', '2024-01-01', 365, 'Diabetes', 110.00, True),
    ('Lisinopril', '2024-02-12', 365, 'Cardiovascular', 140.50, False),
    ('Simvastatin', '2024-02-20', 365, 'Cardiovascular', 160.00, False),
    ('Levothyroxine', '2023-10-15', 365, 'Hormones', 130.00, True),
    ('Amlodipine', '2023-12-25', 540, 'Cardiovascular', 100.00, True),
    ('Cetirizine', '2024-05-18', 365, 'Antihistamine', 80.00, False),
    ('Omeprazole', '2023-09-10', 365, 'Digestive', 90.00, True),
    ('Losartan', '2024-02-17', 540, 'Cardiovascular', 175.00, True),
    ('Clopidogrel', '2024-03-05', 730, 'Cardiovascular', 150.00, True),
    ('Atorvastatin', '2024-01-25', 365, 'Cardiovascular', 125.00, False)
]

for medicine in medicine:
    cursor.execute("""
        INSERT INTO Medicine (name, manufacture_date, shelf_life_days, group_name, price, prescription_required)
        VALUES (%s, %s, %s, %s, %s, %s);
    """, medicine)

suppliers = [
    ('PharmaCo', 'Kyiv, Ukraine', '+380441234567', 'Ivan Petrov', 'Ukraine'),
    ('MedPro', 'Lviv, Ukraine', '+380442345678', 'Olga Ivanova', 'Ukraine'),
    ('BioTech', 'Odessa, Ukraine', '+380443456789', 'Dmytro Sydorenko', 'Ukraine'),
    ('HealthPlus', 'Kharkiv, Ukraine', '+380444567890', 'Yana Lytvynenko', 'Ukraine'),
    ('GlobalMed', 'Poltava, Ukraine', '+380445678901', 'Petro Kuzmenko', 'Ukraine'),
    ('WellnessCorp', 'Dnipro, Ukraine', '+380446789012', 'Anna Romanenko', 'Ukraine'),
    ('PharmaWorld', 'Chernivtsi, Ukraine', '+380447890123', 'Andriy Tymoshenko', 'Ukraine'),
    ('MediLife', 'Ivano-Frankivsk, Ukraine', '+380448901234', 'Svitlana Pavlova', 'Ukraine'),
    ('HealthGroup', 'Sumy, Ukraine', '+380449012345', 'Mykola Shapoval', 'Ukraine'),
    ('BioHealth', 'Ternopil, Ukraine', '+380440123456', 'Oksana Didenko', 'Ukraine'),
    ('PharmaSolutions', 'Vinnytsia, Ukraine', '+380441234567', 'Roman Vasylenko', 'Ukraine'),
    ('EuroMed', 'Zaporizhzhia, Ukraine', '+380442345678', 'Natalia Horbatenko', 'Ukraine'),
    ('PharmaTech', 'Cherkasy, Ukraine', '+380443456789', 'Ihor Lysenko', 'Ukraine'),
    ('WellMed', 'Mykolaiv, Ukraine', '+380444567890', 'Viktor Pashchenko', 'Ukraine'),
    ('GlobalPharma', 'Kherson, Ukraine', '+380445678901', 'Alina Hryshchenko', 'Ukraine')
]

for supplier in suppliers:
    cursor.execute("""
        INSERT INTO Suppliers (supplier_name, address, phone, contact_person, location)
        VALUES (%s, %s, %s, %s, %s);
    """, supplier)

deliveries = [
    ('2024-02-10', 1, 500, 1),
    ('2024-02-12', 2, 600, 2),
    ('2024-02-14', 3, 450, 3),
    ('2024-02-16', 4, 700, 4),
    ('2024-02-18', 5, 350, 5),
    ('2024-02-20', 6, 520, 6),
    ('2024-02-22', 7, 480, 7),
    ('2024-02-24', 8, 650, 8),
    ('2024-02-26', 9, 400, 9),
    ('2024-02-28', 10, 300, 10),
    ('2024-03-02', 11, 720, 11),
    ('2024-03-04', 12, 500, 12),
    ('2024-03-06', 13, 530, 13),
    ('2024-03-08', 14, 470, 14),
    ('2024-03-10', 15, 600, 15)
]

for delivery in deliveries:
    cursor.execute("""
        INSERT INTO Deliveries (delivery_date, medicine_registration_number, quantity, supplier_code)
        VALUES (%s, %s, %s, %s);
    """, delivery)

connection.commit()
cursor.close()
connection.close()
print("Дані успішно додані до таблиць!")
