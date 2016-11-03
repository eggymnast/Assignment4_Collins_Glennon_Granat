import pandas as pd
import re

data = pd.read_excel('06222016 Staph Array Data.xlsx') # read excel file


def parse(s):           # parse column one of data file
    list1 = ['','','']
    vals = s[::-1].split(maxsplit = 2)
    vals = [x[::-1] for x in vals]
    if len(vals) == 2:
        list1[0] = vals[0]
        list1[2] = vals[1]
        return list1
    return vals




test1 = '01 VANDER Serum V2 100'
test2 = '62900 V2    100'
test3 = '62900       100'
test4 = '62129 V2 100'

print(parse(test1), parse(test2), parse(test3), parse(test4))




#print(d)

#map(re.findall(PATTERN),data.ix[:,0])
  #  re.findall(PATTERN,data.ix[row,0])

#re.findall(PATTERN,data.ix[:,0])


#PATTERN = r"(?P<date>\d\d_\d\d_\d\d)_(?P<duration>\d:\d\d:\d\d)_(?P<animal>.*?)_(?P<program>.+).csv"

#print(data)


#PatientID - 23234
#Replicate/visit - V1
#Dilution- 100