import csv
import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

with open("insert_statements_nxg.sql", "r") as sql_file1:
    sql_script1 = sql_file1.read()

with open("insert_statements_gds.sql", "r") as sql_file2:
    sql_script2 = sql_file2.read()

with open("insert_statements_rnf_rec-status.sql", "r") as sql_file3:
    sql_script3 = sql_file3.read()

cursor.executorscript(sql_script3)

with open("insert_statements_rnf_rec_creation_details.sql", "r") as sql_file4:
    sql_script4 = sql_file4.read()

cursor.executorscript(sql_script4)

with open("insert_statements_rnf_error_reason.sql", "r") as sql_file5:
    sql_script5 = sql_file5.read()

cursor.executorscript(sql_script5)
cursor.executorscript(sql_script1)
cursor.executorscript(sql_script2)

conn.commit()
conn.close()

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

try:
    cursor.execute("SELECT process_code from rec_stats")
    rows = cursor.fetchall()

    for row in rows:
        cursor.execute("INSERT INTO rec_errors (process_code) values (?)", (row[0],))

    conn.commit()
    print("DATA copied successfully")

except sqlite3.Error as e:
    print(f"An exception occured: {e}")
finally:
    conn.close()


print("DATA loaded")
