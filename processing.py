import sqlite3 as sq
import pandas as pd
sDataBaseDir='C:/VKHCG/88-DV'
sDatabaseName=sDataBaseDir + '/datavault'
connection=sq.connect(sDatabaseName)
curs=connection.cursor()
student=pd.read_csv('C:/VKHCG/01-Vermeulen/00-RawData/StudentData.csv')
student.to_sql('studentInfo',connection,if_exists='replace',index=False)
curs.execute('select * from studentInfo')
records=curs.fetchall()
for row in records:
    print(row)
connection.close()
