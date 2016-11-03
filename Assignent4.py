import pandas as pd
import re

data = pd.read_excel('06222016 Staph Array Data.xlsx') #read excel file

PATTERN = r"(?P<PatientID>.*) (?P<visit>V?\d?)\s+(?P<dilution>\d+)" #pattern matching test



test1 = '01 VANDER Serum V2 100'
test2 = '62900 V2    100'
test3 = '62900       100'
test4 = '62129 V2 100'



x1 = re.findall(PATTERN,test1)
x2 = re.findall(PATTERN,test2)
x3 = re.findall(PATTERN,test3)
x4 = re.findall(PATTERN,test4)
print(x1, x2, x3, x4)

#print(d)

#map(re.findall(PATTERN),data.ix[:,0])
  #  re.findall(PATTERN,data.ix[row,0])

#re.findall(PATTERN,data.ix[:,0])


#PATTERN = r"(?P<date>\d\d_\d\d_\d\d)_(?P<duration>\d:\d\d:\d\d)_(?P<animal>.*?)_(?P<program>.+).csv"

#print(data)


#PatientID - 23234
#Replicate/visit - V1
#Dilution- 100