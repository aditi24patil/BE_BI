#Data Visualization from Extraction Transformation and Loading (ETL) Process
import pandas as pd
import sqlite3
import openpyxl
conn = sqlite3.connect('student.db')
conn.execute("CREATE TABLE IF NOT EXISTS students (id INT, name TEXT, marks INT)")

# Insert data
conn.execute("INSERT INTO students VALUES (1, 'John', 90)")
conn.execute("INSERT INTO students VALUES (2, 'Hannah', 80)")
conn.commit()

sql_data=pd.read_sql('SELECT * FROM students',conn)

excel_data = pd.read_excel(r"C:\\Users\\Public\sales_data_xlsx.xlsx")
csv_data = pd.read_csv('students.csv')

combined_data = pd.concat([sql_data,csv_data,excel_data])
combined_data=combined_data.drop_duplicates()

print('Combined Data')
print(combined_data)

conn.close()
# ---------------- VISUALIZATION ---------------- #

import matplotlib.pyplot as plt

# Convert marks column to numeric if needed
combined_data['marks'] = pd.to_numeric(combined_data['marks'])

# Bar Chart
plt.figure(figsize=(8,5))

plt.bar(combined_data['name'], combined_data['marks'])

plt.title("Student Marks Visualization")
plt.xlabel("Student Names")
plt.ylabel("Marks")

plt.grid(axis='y')

plt.show()
