import imageio
import pandas as pd
import numpy as np
sInputFileName = 'Angus.jpg'
InputData = imageio.v2.imread(sInputFileName,mode='RGBA')
print('X : ',InputData.shape[0])
print('Y : ',InputData.shape[1])
print('RGBA : ',InputData.shape[2])
ProcessRawData=InputData.flatten()
y=InputData.shape[2] + 2
x=int(ProcessRawData.shape[0]/y)
ProcessData=pd.DataFrame(np.reshape(ProcessRawData,(x,y)))
sColumns = ['XAxis','YAxis','Red','Green','Blue','Alpha']
ProcessData.columns=sColumns
ProcessData.index.names = ['ID']
print('Rows : ',ProcessData.shape[0])
print('Columns : ',ProcessData.shape[1])
OutputData=ProcessData
print('Storing File')
sOutputFileName = 'HORUS-Picture.csv'
OutputData.to_csv(sOutputFileName, index=False)
print('***************************************')
print('Picture to HORUS - Done')
