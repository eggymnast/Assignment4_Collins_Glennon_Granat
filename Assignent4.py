import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


files = pd.read_excel('06222016 Staph Array Data.xlsx', sheetname=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# read excel file into dictionary of dataframes, one for each plate
okay_files = {}
for k, file in files.items():
    file = file.fillna(0)
    okay_files.update({k: file})

columns = list(okay_files[0].ix[0, :])       # generates the list of column names we're interested in
columns[30] = 'SEB_2'
data = okay_files[0][1:]     # remove first line of data sheet
data.columns = columns      # sets the panda columns to the list we generated. Makes it easier to index dataframes
bugs = columns[4:]      # pulls out list of "bugs" (lab tests) we're interested in
bugs_dict = dict.fromkeys(bugs, {})     # makes a dictionary with keys=bugs and values = empty dicts


def parse(s):           # parse column one of data file
    list1 = ['', '', '']
    vals = s[::-1].split(maxsplit=2)
    vals = [x[::-1] for x in vals]
    if len(vals) == 2:
        list1[0] = vals[0]
        list1[1] = 'N/A'
        list1[2] = vals[1]
        return list1[::-1]
    return vals[::-1]

good_files = {}     # using for reformatting data
list_dict = {}      # makes a dict with an entry for each plate, value = parsed first column for that plate
for k, df in okay_files.items():     # passes each key, value tuple from files dictionary of dataframes
    columns = list(df.ix[0, :])

    def uniquify(pasta):      # function to add '_2' to the end of a redundent column name
        seen = set()

        for bug in pasta:
            fudge = 1
            newbug = bug

            while newbug in seen:
                fudge += 1
                newbug = "{}_{}".format(bug, fudge)

            yield newbug
            seen.add(newbug)
    new_columns = list(uniquify(columns))

    data = df[1:]
    data.columns = new_columns
    good_files.update({k: data})

    l = []
    for item in data.ix[:, 0]:
        l.append(parse(item))

    list_dict.update({k: l})


def make_pt_dicts(papa):
    # makes a dictionary with each unique patient ID as a key and a dict of column titles as a key
    unique_pts = {}

    for sublist in papa:
        if sublist[0] != "Standard":
            if sublist[0] != "Sample":
                if sublist[0] not in unique_pts:
                    unique_pts[sublist[0]] = {}

    for pt in unique_pts:
        unique_pts[pt] = bugs_dict

    return unique_pts

big_dict = {}

for k, l in list_dict.items():
    # takes the parsed list for each plate and runs makes patient dictionary out of it,
    # adds the dictionary to big_dict with plate number as key
    data = make_pt_dicts(l)
    big_dict.update({k: data})


def visit_dict(himanshu):       # creates a dictionary with list of visits as value for each patient key
    dict_visit = {}

    for biglist in himanshu.values():
        for sublist in biglist:
            if "Standard" not in sublist[0]:
                if sublist[0] != "Sample":
                    if sublist[0] not in dict_visit:
                        dict_visit[sublist[0]] = {}

    for key in dict_visit.keys():
        empty = []
        for biglist in himanshu.values():
            for sublist in biglist:
                if sublist[0] == key:
                    if sublist[1] not in empty:
                        empty.append(sublist[1])
        dict_visit[key] = empty

    return dict_visit

visits = visit_dict(list_dict)


def add_visits(mark):
    # nests dictionary of visits within each column entry for each patient in patient dictionary within dict entry for
    # each plate

    for plate in mark:
        for pt in mark[plate]:
            if pt in visits.keys():
                for bug in mark[plate][pt]:
                    mark[plate][pt][bug] = dict.fromkeys(visits[pt], {})

    return mark

big_dict = add_visits(big_dict)     # updates big_dict with visit info for each patient


def dilution_dict(jeff):        # makes dictionary of each dilution for each visit for each patient
    dict_dilution = {}

    for biglist in jeff.values():
        for sublist in biglist:
            if 'Standard' not in sublist[0]:
                if sublist[0] != 'Sample':
                    if sublist[0] not in dict_dilution:
                        dict_dilution[sublist[0]] = {}

    for key in dict_dilution.keys():
        empty = []
        for biglist in jeff.values():
            for sublist in biglist:
                if sublist[0] == key:
                    if sublist[2] not in empty:
                        empty.append(sublist[2])
        dict_dilution[key] = empty

    return dict_dilution

dilutions = dilution_dict(list_dict)


def add_dilutions(amanda):      # nests dict of dilutions within each visit for each column for each patient

    for plate in amanda:
        for pt in amanda[plate]:
            if pt in visits.keys():
                for bug in amanda[plate][pt]:
                    for visit in amanda[plate][pt][bug]:
                        amanda[plate][pt][bug][visit] = dict.fromkeys(dilutions[pt], {})

    return amanda

big_dict = add_dilutions(big_dict)      # update big_dict w/ dilution entries for each patient visit

gooder_files = {}       # using for re-reformatting data
for k, df in good_files.items():     # passes each key, value tuple from files dictionary of dataframes
    data = df.set_index('Sample ID')        # sets the first column as index
    # data = data.fillna(0)     # replaces all "NaN" with 0, to make graphing easier
    gooder_files.update({k: data})


def tuple_time(sasha):      # changes the entry for every combination to a tuple that can be graphed
    for plate in sasha:
        for pt in sasha[plate]:
            for bug in sasha[plate][pt]:
                    for visit in sasha[plate][pt][bug]:
                        for dilution in sasha[plate][pt][bug][visit]:
                            x = str(pt) + " " + str(visit) + " " + str(dilution)        # constructs index string
                            if x in list(gooder_files[plate].index):        # compares to indeces in reforated dataframe
                                y = (gooder_files[plate].ix[x, bug])
                                sasha[plate][pt][bug][visit][dilution] = y

    return sasha

big_dict = tuple_time(big_dict)     # final dictionary containing all data to be graphed


def plot_tests(visit, legend_list, pt, bug):        # does the plotting for each graph
    pt = pt
    bug = bug
    title = pt + " - " + bug
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(221)
    fig1, axs = plt.subplots(ncols=1, figsize=(15, 4))
    plt.xscale('log')

    for data_dict in visit.values():
        x = list(data_dict.keys())
        y = list(data_dict.values())
        ax1 = plt.plot(x, y, x, y, 'o')
        plt.title(title)
        plt.xlabel('Dilution')
        plt.ylabel('Intensity')
        plt.legend(legend_list, loc='best', frameon=bool)

    return fig1


def access_plates(sasha):       # iterates through dictionary and generates column title, patient, and #visits to plot
    for plate in sasha:
        for pt in sasha[plate]:
            for bug in sasha[plate][pt]:
                legend_list = sasha[plate][pt][bug].keys()
                fig = plot_tests((sasha[plate][pt][bug]), legend_list, pt, bug)
                fig.savefig(pt+bug, format='png')

access_plates(big_dict)

for k, v in list_dict.items():         # fixes cases where parsing function fails
    for sub_v in v:
        if len(sub_v) != 3:
            sub_v.append('N/A')
            sub_v.append('UNKOWN')

new_dict = {}       # Makes dict easier to modify before final export
for k, file in files.items():
    columns = list(file.ix[0, :])
    data = file
    data.columns = columns
    new_dict.update({k: data})


final_wow = {}
for k, data in new_dict.items():
    column_1 = []
    for l in list_dict[k]:
        column_1.append(l[0])
    column_2 = []
    for l in list_dict[k]:
        column_2.append(l[1])
    column_3 = []
    for l in list_dict[k]:
        column_3.append(l[2])
    first_three = pd.DataFrame({'Patient ID': column_1, 'Visit': column_2, 'Dilutions': column_3})
    cols = ['Patient ID', 'Visit', 'Dilutions']
    first_three = first_three[cols]     # rearranges columns in new dataframe to be in correct order
    last_cols = data.ix[:, 1:]
    merged = pd.concat([first_three, last_cols], axis=1, ignore_index=False)
    # makes merged dataframe for each plate
    print(merged)
    final_wow.update({k: merged})


for k, data in final_wow.items():       #saves tab-delimited files of each plate
    data.to_csv('Plate-'+str(k)+'.txt', sep='\t')