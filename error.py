import pandas as pd
sName='Assess-raw.csv'
RawData=pd.read_csv(sName,header=0)
print(RawData)
print('Rows:',RawData.shape[0])
print('Columns:',RawData.shape[1])
CleanData=RawData.dropna(axis=1,how='all')
print(CleanData)
print('Rows:',CleanData.shape[0])
print('Columns:',CleanData.shape[1])
CleanData=RawData.dropna(axis=1,how='any')
print(CleanData)
print('Rows:',CleanData.shape[0])
print('Columns:',CleanData.shape[1])
CleanData=RawData.dropna(thresh=2)
print(CleanData)
print('Rows:',CleanData.shape[0])
print('Columns:',CleanData.shape[1])
CleanData.to_csv('CleanedData.csv',index=False)