import pandas as pd
InputFileName = 'StudentData.csv'
StudentData=pd.read_csv(InputFileName,header=0)
print(StudentData.shape[0])
print(StudentData.shape[1])
StudentData.rename(columns={'gre':'GRE'},inplace=True)
AllData=StudentData[['name','qr','GRE']]
MeanData=AllData['GRE'].mean()
StdData=AllData['GRE'].std()
print('Outliers')
UpperBound=float(MeanData+StdData)
print('Higher than ', UpperBound)
OutliersHigher=AllData[AllData.GRE>UpperBound]
print(OutliersHigher)
LowerBound=float(MeanData-StdData)
print('Lower than ',LowerBound)
OutliersLower=AllData[AllData.GRE<LowerBound]
print(OutliersLower)
