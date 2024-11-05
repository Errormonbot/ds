import pandas as pd

sInputFileName='Country_Code.json'
ProcessData = pd.read_json(sInputFileName,orient='index')
print(ProcessData)

ProcessData.drop('ISO-2-CODE',axis=1,inplace=True)
ProcessData.drop('ISO-3-Code',axis=1,inplace=True)

ProcessData.rename(columns={'Country':'CountryName'},inplace=True)
ProcessData.rename(columns={'ISO-M49':'CountryNumber'},inplace=True)

ProcessData.set_index('CountryName',inplace=True)
ProcessData.sort_values('CountryName',axis=0,ascending=False,inplace=True)

print(ProcessData)
sOutputFileName='HORUS-JSON-Coutry.csv'
ProcessData.to_csv(sOutputFileName,index=False)
print('JSON to HORUS - Done')
