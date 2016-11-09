from matplotlib import pyplot as plt

sample = {0:{'23234':{'Exoprotein ext': {'V2': {100000: 290.5, 10000: 1432.5, 1000: 4725.5, 100: 6746.0}}}}}


easy_test = {'V2': {100000: 290.5, 10000: 1432.5, 1000: 4725.5, 100: 6746.0}}


def plot_tests(visit, legend_list, pt, bug):
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
        ax1 = plt.plot(x, y, x, y, 'bo')
        plt.title(title)
        plt.xlabel('Dilution')
        plt.ylabel('Intensity')
        plt.legend(legend_list, loc='best', frameon=bool)
    return fig1



def access_plates(sasha):
    for plate in sasha:
        for pt in sasha[plate]:
            for bug in sasha[plate][pt]:
                legend_list = sasha[plate][pt][bug].keys()
                fig = plot_tests((sasha[plate][pt][bug]), legend_list, pt, bug)
                fig.savefig(pt+bug, format='png')

access_plates(sample)


# ax1 = data.ix[:,0:5].plot(kind = 'line', ax = axs[0])
# ax1.set_title('HMECprolif_1250')
# ax1.set_xlabel('time')
# ax1.set_ylabel('absorbance')
# ax1.legend(title = 'Legend', loc = 0)

# fig1.savefig('Figure 1.png')

# PSMalpha2