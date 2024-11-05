#prerequisite bmi.py

import pandas as pd
import sqlite3 as sq

# Database connection
sDatabaseName = 'datavault.db'
conn1 = sq.connect(sDatabaseName)

t = 0
tMax = ((200 - 100) / 10) * ((200 - 30) / 5)
data = []  # Create a list to store the data

for heightSelect in range(100, 200, 10):
    for weightSelect in range(30, 200, 5):
        height = round(heightSelect / 100, 3)
        weight = int(weightSelect)
        bmi = weight / (height * height)

        if bmi <= 18.5:
            BMI_Result = 1
        elif 18.5 < bmi < 25:
            BMI_Result = 2
        elif 25 < bmi < 30:
            BMI_Result = 3
        elif bmi >= 30:
            BMI_Result = 4
        else:
            BMI_Result = 0
        
        # Collect data in a list of dictionaries
        data.append({
            'PersonID': str(t),
            'Height': height,
            'Weight': weight,
            'bmi': bmi,
            'Indicator': BMI_Result
        })
        
        t += 1
        print('Row:', t, 'of', tMax)

# Create DataFrame from the list of dictionaries
DimPerson = pd.DataFrame(data)

# Store in SQLite database
sTable = 'BMI'
print('\n#################################')
print('Storing :', sDatabaseName, '\n Table:', sTable)
print('\n#################################')
DimPerson.to_sql(sTable, conn1, if_exists="replace", index=False)

# Close the database connection
conn1.close()


#Note: new datavault.db file be created in the same folder that of bmi.py
 
#Go to https://www.sqlite.org/download.html and
#download sqlite-tools-win-x64-3460100.zip
#and extract and open sqlite3
 
#And perform the command
#.open \\datavault.db
#.tables
#select * from BMI;

##############

#HORIZONTAL DATAVAULT
import pandas as pd
import sqlite3 as sq
sDatabaseName='C:/Users/Student/Downloads/datavault.db'
conn1=sq.connect(sDatabaseName)
sTable='BMI'
print('Loading:',sDatabaseName,'Table:',sTable)
sSQL='SELECT * FROM [BMI];'
PersonFrame0=pd.read_sql_query(sSQL,conn1)
sSQL="SELECT *\
    FROM [BMI] \
    WHERE Height > 1.6 and Indicator=2\
     ORDER BY \
     Height,\
     Weight;"
PersonFrame1=pd.read_sql_query(sSQL,conn1)
sTable='BMI_Horizontal'
print('Loading:',sDatabaseName,'Table:',sTable)
print('Full Data Set (ROWS):',PersonFrame0.shape[0])
print('FULL DATA SET COLUMNS):',PersonFrame0.shape[1])
print('#####################################')
print('Horizontal Data Set (ROWS):',PersonFrame1.shape[0])
print('Horizontal DATA SET COLOUMNS):',PersonFrame1.shape[1])

#Vertical DATAVAULT
import pandas as pd
import sqlite3 as sq
sDatabaseName='C:/Users/Student/Downloads/datavault.db'
conn1=sq.connect(sDatabaseName)
sTable='BMI'
print('Loading:',sDatabaseName,'Table:',sTable)
sSQL='SELECT * FROM [BMI];'
PersonFrame0=pd.read_sql_query(sSQL,conn1)
sSQL="SELECT Height,Weight,Indicator\
    FROM [BMI];"
PersonFrame1=pd.read_sql_query(sSQL,conn1)
sTable='BMI_Vertical'
print('Loading:',sDatabaseName,'Table:',sTable)
print('Full Data Set (ROWS):',PersonFrame0.shape[0])
print('FULL DATA SET COLUMNS):',PersonFrame0.shape[1])
print('#####################################')
print('Horizontal Data Set (ROWS):',PersonFrame1.shape[0])
print('Horizontal DATA SET COLOUMNS):',PersonFrame1.shape[1])


#SECURE
import pandas as pd
import sqlite3 as sq
sDatabaseName='C:/Users/rohit/Downloads/datavault.db'
conn1 = sq.connect(sDatabaseName)
sTable = 'BMI'
print('Loading :',sDatabaseName,' Table:',sTable)
sSQL="SELECT * FROM [BMI];"
PersonFrame0=pd.read_sql_query(sSQL, conn1)
sSQL="SELECT \
       Height,\
       Weight,\
       Indicator,\
       CASE Indicator\
       WHEN 1 THEN 'Paul'\
       WHEN 2 THEN 'Norman'\
       WHEN 3 THEN 'Thomas'\
       ELSE 'Sam'\
       END AS Name\
  FROM [BMI]\
  WHERE Indicator > 2\
  ORDER BY  \
       Height,\
       Weight;"
PersonFrame1=pd.read_sql_query(sSQL, conn1)
sTable = 'BMI_Secure'
PersonFrame1.to_sql(sTable, conn1, if_exists="replace")
print('Storing :',sDatabaseName,'\n Table:',sTable)
sSQL="SELECT * FROM [BMI_Secure] WHERE Name = 'Sam';"
PersonFrame2=pd.read_sql_query(sSQL, conn1)
################################################################
print('################################')
print('Full Data Set (Rows):', PersonFrame0.shape[0])
print('Full Data Set (Columns):', PersonFrame0.shape[1])
print('################################')
print('Secure Data Set (Rows):', PersonFrame2.shape[0])
print('Secure Data Set (Columns):', PersonFrame2.shape[1])
print('Only Sam Data')
print(PersonFrame2.head())
print('################################')


