import pandas as pd
from matplotlib import pyplot as plt
from collections import defaultdict

data = pd.read_excel('06222016 Staph Array Data.xlsx') # read excel file
bugs = list(data.ix[0, 4::])
bugsdict = dict.fromkeys(bugs, {})
data = data[1:] # remove first line of data sheet


def parse(s):           # parse column one of data file
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

print(l)

def visit_dict(himanshu):
    dict_visit = {}

    for sublist in himanshu:
        if sublist[0] != "Standard":
            if sublist[0] not in dict_visit:
                dict_visit[sublist[0]] = {}

    for key in dict_visit.keys():
        empty = []
        for sublist in himanshu:
            if sublist[0] == key:
                if sublist[1] not in empty:
                    empty.append(sublist[1])
        dict_visit[key] = empty

    return dict_visit

visits = visit_dict(l)


def dilution_dict(jeff):
    dict_dilution = {}

    for sublist in jeff:
        if sublist[0] != "Standard":
            if sublist[0] not in dict_dilution:
                dict_dilution[sublist[0]] = {}

    for key in dict_dilution.keys():
        empty = []
        for sublist in jeff:
            if sublist[0] == key:
                if sublist[2] not in empty:
                    empty.append(sublist[2])
        dict_dilution[key] = empty

    return dict_dilution

dilutions = dilution_dict(l)
print(dilutions)

def make_pt_dicts(list):
    unique_pts = {}

    for sublist in list:
        if sublist[0] != "Standard":
            if sublist[0] not in unique_pts:
                unique_pts[sublist[0]] = {}

    for pt in unique_pts:
        unique_pts[pt] = bugsdict

    return unique_pts

def add_visits(mark):

    for pt in mark:
        for bug in mark[pt]:
            mark[pt][bug] = dict.fromkeys(visits[pt], {})

    return mark

def add_dilutions(amanda):
    for pt in amanda:
        for bug in amanda[pt]:
            for visit in amanda[pt][bug]:
                amanda[pt][bug][visit] = dict.fromkeys(dilutions[pt], {})


    return amanda


test1 = add_dilutions(add_visits(make_pt_dicts(l)))
print(test1)



def graph_df(l, df):
    newdf.index = l[2]
    newdf.columns = l[1]


#fig1 = plt.figure()
#ax1 = fig1.add_subplot(221)
#fig1, axs = plt.subplots(ncols=1, figsize=(15,4))


#ax1 = data.ix[:,0:5].plot(kind = 'line', ax = axs[0])
#ax1.set_title('HMECprolif_1250')
#ax1.set_xlabel('time')
#ax1.set_ylabel('absorbance')
#ax1.legend(title = 'Legend', loc = 0)

#fig1.savefig('Figure 1.png')

#PSMalpha2





#print(data)


