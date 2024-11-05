import pandas as pd
InputFileName = 'StudentData.csv'
print('Loading : ',InputFileName)
StudentData = pd.read_csv(InputFileName,header=0)
StudentData.rename(columns={'gre': 'GRE'},inplace=True)
AllData=StudentData[['name','qr','GRE']]
print(AllData)
MeanData=AllData['GRE'].mean()
print(MeanData)
MeanData=AllData.groupby(['qr'])['GRE'].mean()
print(MeanData)
