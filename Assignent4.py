import pandas as pd
from matplotlib import pyplot as plt

files = pd.read_excel('06222016 Staph Array Data.xlsx',sheetname=[0,1,2,3,4,5,6,7,8,9,10])
# read excel file into dictionary of dataframes, one for each plate

columns = list(files[0].ix[0, :])
data = files[0][1:]     # remove first line of data sheet
data.columns = columns
bugs = columns[4:]
bugs_dict = dict.fromkeys(bugs, {})


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
for item in data.ix[:, 0]:
    l.append(parse(item))


def make_pt_dicts(papa):
    #makes a dictionary with each unique patient ID as a key and a dict of column titles as a key
    unique_pts = {}

    for sublist in papa:
        if sublist[0] != "Standard":
            if sublist[0] not in unique_pts:
                unique_pts[sublist[0]] = {}

    for pt in unique_pts:
        unique_pts[pt] = bugs_dict

    return unique_pts


def visit_dict(himanshu):       #creates a dictionary with list of visits as value for each patient key
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


def add_visits(mark):       #nests dictionary of visits within each column entry for each patient in patient dictionary

    for pt in mark:
        for bug in mark[pt]:
            mark[pt][bug] = dict.fromkeys(visits[pt], {})

    return mark


def dilution_dict(jeff):        #makes dictionary of each dilution for each visit for each patient
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


def add_dilutions(amanda):      #nests dict of dilutions within each visit for each column for each patient
    for pt in amanda:
        for bug in amanda[pt]:
            for visit in amanda[pt][bug]:
                amanda[pt][bug][visit] = dict.fromkeys(dilutions[pt], {})

    return amanda

data = data.set_index(['Sample ID'])
data = data.fillna(0)


def tuple_time(sasha):      #changes the entry for every combination to a tuple that can be graphed
    for pt in sasha:
        for bug in sasha[pt]:
            for visit in sasha[pt][bug]:
                for dilution in sasha[pt][bug][visit]:
                    x = str(pt) + " " + str(visit) + " " + str(dilution)
                    if x in list(data.index):
                        y = str(data.ix[x, bug])
                        sasha[pt][bug][visit][dilution] = (dilution, y)     #add reg. expression to exclude non-numbers

    return sasha


test = add_dilutions(add_visits(make_pt_dicts(l)))
test1 = tuple_time(test)
print(test1)


#def graph_df(l, df):
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


