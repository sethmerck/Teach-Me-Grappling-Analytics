import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt 

# Establish connection to the MySQL database
mydb = mysql.connector.connect(host="localhost", user="root", passwd="yourpassword")

# Create a cursor to execute the SQL queries
mycursor = mydb.cursor()

# Get the list of tables from the database
mycursor.execute("USE grapdb")
mycursor.execute("SHOW TABLES")
tables = mycursor.fetchall()

# Iterate over the list of tables to perform statistical analysis
median = {}
mean = {}
for table in tables:
    mycursor.execute("SELECT * FROM %s" % table)
    results = mycursor.fetchall()
    
    # Create a Pandas dataframe from the MySQL result
    df = pd.DataFrame(results)
    
    # Perform statistical analysis on the dataframe
    median[table[0]] = df[1].median()
    mean[table[0]] = df[1].mean()

median['All'] = median.pop('whole_table')
mean['All'] = mean.pop('whole_table')

# list of keys 
keys = list(median.keys()) 
  
# list of values 
med_values = list(median.values()) 
mean_values = list(mean.values())

# plotting the points  
plt.figure(figsize=(20,6)) 
plt.bar(keys, med_values)
plt.bar(keys, mean_values, width=0.5)

# naming the x-axis 
plt.xlabel('Channel') 
# naming the y-axis 
plt.ylabel('Median Views') 
  
# giving a title to the graph 
plt.title('Bar Graph') 
  
# function to show the plot 
plt.show()
