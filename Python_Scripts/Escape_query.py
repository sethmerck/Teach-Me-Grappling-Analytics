import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt 

# Establish connection to the MySQL database
mydb = mysql.connector.connect(host="localhost", user="root", passwd="your_password")

# Create a cursor to execute the SQL queries
mycursor = mydb.cursor()

# Get the list of tables from the database
mycursor.execute("USE grapdb")
mycursor.execute("SHOW TABLES")
tables = mycursor.fetchall()

# Iterate over the list of tables to perform statistical analysis
esc_median = {}
oth_median = {}
counts = []
for table in tables:

    mycursor.execute(f"SELECT title, views FROM {table[0]} WHERE UPPER(title) LIKE UPPER('%Escape%');")
    esc_results = mycursor.fetchall()
    mycursor.execute(f"SELECT COUNT(*) FROM {table[0]} WHERE UPPER(title) LIKE UPPER('%Escape%');")
    esc_count = mycursor.fetchall()[0][0]
    mycursor.execute(f"SELECT title, views FROM {table[0]} WHERE UPPER(title) NOT LIKE UPPER('%Escape%');")
    oth_results = mycursor.fetchall()
    mycursor.execute(f"SELECT COUNT(*) FROM {table[0]} WHERE UPPER(title) NOT LIKE UPPER('%Escape%');")
    oth_count = mycursor.fetchall()[0][0]
    counts.append((esc_count, oth_count))

    # Create a Pandas dataframe from the MySQL result
    esc_df = pd.DataFrame(esc_results)
    oth_df = pd.DataFrame(oth_results)

    # Perform statistical analysis on the dataframe
    esc_median[table[0]] = esc_df[1].median()
    oth_median[table[0]] = oth_df[1].median()

esc_median['All'] = esc_median.pop('whole_table')
oth_median['All'] = oth_median.pop('whole_table')

# list of keys 
keys = list(esc_median.keys()) 
  
# list of values 
esc_med_values = list(esc_median.values()) 
oth_med_values = list(oth_median.values())

# plotting the points  
plt.figure(figsize=(15,6)) 
plt.bar(keys, esc_med_values)
for i, v in enumerate(counts):
    plt.text(i-0.2, esc_med_values[i] + 900, f'n = {str(v[0])}', fontsize=10)

plt.bar(keys, oth_med_values, width=0.5)
for i, v in enumerate(counts):
    plt.text(i-0.2575, oth_med_values[i] * 0.425, f'n = {str(v[1])}', fontsize=10)

# naming the x-axis 
plt.xlabel('Channel') 
# naming the y-axis 
plt.ylabel('Median View Count') 
  
# giving a title to the graph 
plt.title('Median Views of Videos About Escapes vs. All Other Videos') 
plt.legend(['Esc in Title', 'All Other Videos'])

# function to show the plot 
plt.savefig('escapes_table_stats.png')
