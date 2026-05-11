#mport Data from different Sources such as (Excel, Sql Server, Oracle etc.) and load in targeted system
import pandas as pd
import sqlite3
import openpyxl
# ---------------- DATABASE CONNECTION ----------------
conn = sqlite3.connect('student.db')
# Create table
conn.execute("""
CREATE TABLE IF NOT EXISTS students
(id INT, name TEXT, marks INT)
""")

# Insert records
conn.execute("INSERT INTO students VALUES (1, 'John', 90)")
conn.execute("INSERT INTO students VALUES (2, 'Hannah', 80)")

conn.commit()
sql_data = pd.read_sql('SELECT * FROM students',
    conn
)

excel_data = pd.read_excel(r"C:\\Users\\Public\\sales_data_xlsx.xlsx")
csv_data = pd.read_csv('students.csv')
combined_data = pd.concat([sql_data, csv_data, excel_data])
combined_data = combined_data.drop_duplicates()
combined_data.to_csv('final_dataset.csv',
    index=False
)
print("Final Combined Dataset :")
print(combined_data)
conn.close()
