import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import norm
from sklearn.neighbors import KernelDensity

##############################

# uploading csv data for the CAIs
url = "https://raw.githubusercontent.com/f-jorge/f-jorge.github.io/main/Al26_CAIs_data%20-%2026Al_27Al.csv"
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
    m, bins, patches = ax1.hist(x_train, bins=10, color = 'lightblue', edgecolor = 'cornflowerblue')
    ax1.set_xticks(bins)
    ax1.set_xlabel('26Al/27Al')
    ax1.set_ylabel('count')
    ax1.set_title('All CAI, All Chondrites')

#################
    #KDE
    # for x_test the minimum value in the array and the max value will create the x-axis
    # the n value will dictate how many points its going to do kde on, so all of the values

    x_test = np.linspace(minimum, maximum, n)[:, np.newaxis]

    # the following code is using the kerneldensity function and fitting it to our data

    #model = KernelDensity(kernel = 'gaussian').fit(n_numpy_array)
    #log_dens = model.score_samples(x_test)
    #ax2.fill(x_test, np.exp(log_dens), c='lightgrey')
    ax2.set_xlabel('26Al/27Al')
    #ax2.set_ylabel('value')
    ax2.set_title('Kernel Density Estimation')

# only want one kde line plotted
    # this code is plotting a few different kde types... we only want gaussian
    # Plot a 1D density example

    #true_dens = 0.3 * norm(0, 1).pdf(x_test[:, 0]) + 0.7 * norm(5, 1).pdf(x_test[:, 0])

    # you can add back in the input distribution here and the other kde types
    #ax2.fill(x_test[:, 0], true_dens, fc="black", alpha=0.2, label="input distribution")
    #colors = ["navy", "cornflowerblue", "darkorange"]
    #kernels = ["gaussian", "tophat", "epanechnikov"]

    # this is for only the gaussian distribution
    color = ["pink"]
    kernel = ["gaussian"]
    lw = 2

# this is adding in the line plot version of the kde distribution rather than filled in input distribution
    for color, kernel in zip(color, kernel):
        kde = KernelDensity(kernel=kernel, bandwidth=0.5).fit(n_numpy_array)
        log_dens = kde.score_samples(x_test)
        ax2.plot(
            x_test[:, 0],
            np.exp(log_dens),
            color=color,
            lw=lw,
            linestyle="-",
            label="kernel = '{0}'".format(kernel),
        )

    ax2.legend(loc="upper left")
    plt.show()
al26_all()


# other chondrite types that can be used for data for plots
CO3_0 = data.loc[data['chondrite type'] == 'CO3.0']
CV3 = data.loc[data['chondrite type'] == 'CV3']
CM2 = data.loc[data['chondrite type'] == 'CM2']
CR2 = data.loc[data['chondrite type'] == 'CR2']

#################################################################################

