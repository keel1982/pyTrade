'''
@author: Admin
'''
from WindPy import *
import sqlite3
import numpy as np
Stime='2015-11-1 09:14:59'
Etime='2015-11-30 15:15:01'

w.start()
instrument='TF00.CFE'
data=w.wsi(instrument,'open,high,low,close,volume',Stime,Etime,'BarSize=1')
conn=sqlite3.connect('test.db')
 #(Timestamp,Instrument,Open,High,Low,Close,Volume)


i=0
for d in data.Times:
  timestamp=d
  open=data.Data[0][i]
  high=data.Data[1][i]
  low=data.Data[2][i]
  close=data.Data[3][i]
  volume=data.Data[4][i]
  if(not np.isnan(open) and not volume ==0 ):
   cmd= "INSERT INTO Data VALUES (\'"+timestamp.strftime("%Y-%m-%d %H:%M:%S")+"\',\'"+instrument+"\',"+str(open)+","+str(high)+","+str(low)+","+str(close)+","+str(volume)+")"
   #print(cmd)
   conn.execute(cmd)
  i+=1
conn.commit()
w.stop()

if __name__ == '__main__':
    pass