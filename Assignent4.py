import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_excel('06222016 Staph Array Data.xlsx') # read excel file
data = data[1:] # remove first line of data sheet

print(data.index)

def parse(s: object) -> object:           # parse column one of data file
    list1 = ['','','']
    vals = s[::-1].split(maxsplit = 2)
    vals = [x[::-1] for x in vals]
    if len(vals) == 2:
        list1[0] = vals[0]
        list1[2] = vals[1]
        return list1[::-1]
    return vals[::-1]

l = []
for item in data.ix[:,0]:
    l.append(parse(item))

def graph_df(l, df):
    newdf.index = l[2]
    newdf.columns = l[1]


fig1 = plt.figure()
ax1 = fig1.add_subplot(221)
fig1, axs = plt.subplots(ncols=1, figsize=(15,4))


#ax1 = data.ix[:,0:5].plot(kind = 'line', ax = axs[0])
#ax1.set_title('HMECprolif_1250')
#ax1.set_xlabel('time')
#ax1.set_ylabel('absorbance')
#ax1.legend(title = 'Legend', loc = 0)

#fig1.savefig('Figure 1.png')

#PSMalpha2


test1 = '01 VANDER Serum V2 100'
test2 = '62900 V2    100'
test3 = '62900       100'
test4 = '62129 V2 100'

print(parse(test1), parse(test2), parse(test3), parse(test4))






#print(data)


