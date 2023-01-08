import csv
import mysql.connector
 
mydb = mysql.connector.connect(host='localhost',
    user='root',
    passwd='your_password',
    db='your_db')
cursor = mydb.cursor()
query = "CREATE TABLE your_table (title VARCHAR(255),views INT,whe VARCHAR(255),href VARCHAR(255));"
cursor.execute(query)

with open('your_csv.csv') as file_obj:
    csv_data = csv.reader(file_obj)
    for row in csv_data:
        cursor.execute('INSERT INTO your_table VALUES("%s", "%s", "%s", "%s")',[row[0],int(row[1]),row[2],row[3]])

#close the connection to the database.
mydb.commit()
cursor.close()
print("Done")