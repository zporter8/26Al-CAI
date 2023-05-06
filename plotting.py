import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.neighbors import KernelDensity

##############################

# uploading csv data for the CAIs
url = "https://raw.githubusercontent.com/f-jorge/CAI-project/new_branch/CAI-project/Al26_CAIs_data%20-%2026Al_27Al.csv"
data = pd.read_csv(url, index_col=0)


# 27Al/26Al ratio (x-axis) vs. number of CAIs (y-axis)
def al26_all():
    x = data["26Al/27Al"]
    x_train = []
    # reducing the data to only numerical values by removing words
    for i in x:
        if isinstance(i, str):
            # if i[0] != 'M':
            if not i.isalpha() and i[0] != 'M':
                x_train.append(i)
    x_train.sort()
    # found the length of the dataset
    n = len(x_train)
    # the minimum and maximum values have to be float
    minimum = float(min(x_train))
    maximum = float(max(x_train))
    # need to reshape the data because it expected a 2D array and got a 1D array
    # you can't reshape a list, so you have to change it to an array
    numpy_array = np.array(x_train)
    # we want to check what the array looks like and the shape of it before we reshape it
    # print(numpy_array)
    # print(numpy_array.shape)
    # here we reshaped the array after seeing its original shape
    n_numpy_array = numpy_array.reshape(-1, 1)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[10,5])
    # histogram
    m, bins, patches = ax1.hist(x_train, bins=10, color = 'lightgrey', edgecolor = 'grey')
    ax1.set_xticks(bins)
    ax1.set_xlabel('26Al/27Al')
    ax1.set_ylabel('count')
    ax1.set_title('All CAI, All Chondrites')

    #KDE
    # for x_test the minimum value in the array and the max value will create the x-axis
    # the n value will dictate how many points its going to do kde on, so all of the values
    x_test = np.linspace(minimum, maximum, n)[:, np.newaxis]
    # the following code is using the kerneldensity function and fitting it to our data
    model = KernelDensity()
    model.fit(n_numpy_array)
    log_dens = model.score_samples(x_test)
    ax2.fill(x_test, np.exp(log_dens), c='lightgrey')
    ax2.set_xlabel('26Al/27Al')
    ax2.set_ylabel('value')
    ax2.set_title('Kernel Density Estimation')
    plt.show()
#al26_all()

def al26_CO3():
    CO3_0 = data.loc[data['type'] == 'CO3.0']
    x = CO3_0["26Al/27Al"]
    x_train = []
    for i in x:
        if isinstance(i, str):
            # if i[0] != 'M':
            if not i.isalpha() and i[0] != 'M':
                x_train.append(i)
    x_train.sort()
    n = len(x_train)
    minimum = float(min(x_train))
    maximum = float(max(x_train))
    numpy_array = np.array(x_train)
    n_numpy_array = numpy_array.reshape(-1, 1)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[10,5])
    # histogram
    m, bins, patches = ax1.hist(x_train, bins=10, color = 'lightgrey', edgecolor = 'grey')
    ax1.set_xticks(bins)
    ax1.set_xlabel('26Al/27Al')
    ax1.set_ylabel('count')
    ax1.set_title('All CAI, CO3 Chondrites')

    #KDE
    x_test = np.linspace(minimum, maximum, n)[:, np.newaxis]
    model = KernelDensity()
    model.fit(n_numpy_array)
    log_dens = model.score_samples(x_test)
    ax2.fill(x_test, np.exp(log_dens), c='lightgrey')
    ax2.set_xlabel('26Al/27Al')
    ax2.set_ylabel('value')
    ax2.set_title('Kernel Density Estimation')
    plt.show()
#al26_CO3()


def al26_CV3():
    CV3 = data.loc[data['type'] == 'CV3']
    x = CV3["26Al/27Al"]
    x_train = []
    for i in x:
        if isinstance(i, str):
            # if i[0] != 'M':
            if not i.isalpha() and i[0] != 'M':
                x_train.append(i)
    x_train.sort()
    n = len(x_train)
    minimum = float(min(x_train))
    maximum = float(max(x_train))
    numpy_array = np.array(x_train)
    n_numpy_array = numpy_array.reshape(-1, 1)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[10,5])
    # histogram
    m, bins, patches = ax1.hist(x_train, bins=10, color = 'lightgrey', edgecolor = 'grey')
    ax1.set_xticks(bins)
    ax1.set_xlabel('26Al/27Al')
    ax1.set_ylabel('count')
    ax1.set_title('All CAI, CV3 Chondrites')

    #KDE
    x_test = np.linspace(minimum, maximum, n)[:, np.newaxis]
    model = KernelDensity()
    model.fit(n_numpy_array)
    log_dens = model.score_samples(x_test)
    ax2.fill(x_test, np.exp(log_dens), c='lightgrey')
    ax2.set_xlabel('26Al/27Al')
    ax2.set_ylabel('value')
    ax2.set_title('Kernel Density Estimation')
    plt.show()
#al26_CV3()

def al26_CM2():
    CM2 = data.loc[data['type'] == 'CM2']
    x = CM2["26Al/27Al"]
    x_train = []
    for i in x:
        if isinstance(i, str):
            # if i[0] != 'M':
            if not i.isalpha() and i[0] != 'M':
                x_train.append(i)
    x_train.sort()
    n = len(x_train)
    minimum = float(min(x_train))
    maximum = float(max(x_train))
    numpy_array = np.array(x_train)
    n_numpy_array = numpy_array.reshape(-1, 1)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[10,5])
    # histogram
    m, bins = patches = ax1.hist(x_train, bins=10, color = 'lightgrey', edgecolor = 'grey')
    ax1.set_xticks(bins)
    ax1.set_xlabel('26Al/27Al')
    ax1.set_ylabel('count')
    ax1.set_title('All CAI, CM2 Chondrites')

    #KDE
    x_test = np.linspace(minimum, maximum, n)[:, np.newaxis]
    model = KernelDensity()
    model.fit(n_numpy_array)
    log_dens = model.score_samples(x_test)
    ax2.fill(x_test, np.exp(log_dens), c='lightgrey')
    ax2.set_xlabel('26Al/27Al')
    ax2.set_ylabel('value')
    ax2.set_title('Kernel Density Estimation')
    plt.show()
#al26_CM2()

def al26_CR2():
    CR2 = data.loc[data['type'] == 'CR2']
    x = CR2["26Al/27Al"]
    x_train = []
    for i in x:
        if isinstance(i, str):
            # if i[0] != 'M':
            if not i.isalpha() and i[0] != 'M':
                x_train.append(i)
    x_train.sort()
    n = len(x_train)
    minimum = float(min(x_train))
    maximum = float(max(x_train))
    numpy_array = np.array(x_train)
    n_numpy_array = numpy_array.reshape(-1, 1)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[10,5])
    # histogram
    m, bins, patches = ax1.hist(x_train, bins=10, color = 'lightgrey', edgecolor = 'grey')
    ax1.set_xticks(bins)
    ax1.set_xlabel('26Al/27Al')
    ax1.set_ylabel('count')
    ax1.set_title('All CAI, CR2 Chondrites')

    #KDE
    x_test = np.linspace(minimum, maximum, n)[:, np.newaxis]
    model = KernelDensity()
    model.fit(n_numpy_array)
    log_dens = model.score_samples(x_test)
    ax2.fill(x_test, np.exp(log_dens), c='lightgrey')
    ax2.set_xlabel('26Al/27Al')
    ax2.set_ylabel('value')
    ax2.set_title('Kernel Density Estimation')
    plt.show()
#al26_CR2()

#################################################################################

