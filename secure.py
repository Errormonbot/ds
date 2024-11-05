import pandas as pd
import sqlite3 as sq
sDatabaseName='datavault.db'
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
