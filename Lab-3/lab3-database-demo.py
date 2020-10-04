#!/usr/bin/env python3
import sqlite3
#connect to database file
dbconnect = sqlite3.connect("main.db");
#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();
#execute insert statement
cursor.execute('''insert into temps values ('01-Jan', '12:01 PM', 'kitchen', 21.0)''');
dbconnect.commit();
#execute simple select statement
cursor.execute('SELECT * FROM temps');
#print data
for row in cursor:
    print(row['tdate'],row['ttime'],row['zone'],row['temperature'] );
#close the connection

cursor.execute('DELETE FROM temps');
dbconnect.commit();
#Creating the sedond table (sensor)
cursor.execute('create table if not exists sensors(sensorID integer, type text, zone text)');
cursor.execute('delete from sensors');
dbconnect.commit();

typeInit = ["door", "temperature", "door", "motion", "temperature"];
zoneInit = ["kitchen", "kitchen", "garage", "garage", "garage"];

for i in range(5):
    command = "insert into sensors values (" + str(i+1) + ", '" + typeInit[i] + "', '" + zoneInit[i] + "')";
    cursor.execute(command);
    dbconnect.commit();

cursor.execute('select * from sensors');

#for row in cursor:
#    print(row['sensorID'], row['type'], row['zone'])
#print("");

print("Searching for all sensors in the kitchen:");
cursor.execute("select * from sensors where zone = 'kitchen'");
for row in cursor:
    print(row['sensorID'], row['type'], row['zone'])
print("");


print("Searching for all door sensors:");
cursor.execute("select * from sensors where type = 'door'");
for row in cursor:
    print(row['sensorID'], row['type'], row['zone'])
print("");


dbconnect.close();
