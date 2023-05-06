import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("/Users/fatima/Desktop/EART119B/Isotopic-CAI-data.csv")

#CO3 chondrites example
CO3_0 = data.loc[data['type'] == 'CO3.0']
x = CO3_0["26Al/27Al"]
list = []
# reducing the data to only numerical values by removing words
for i in x:
       if isinstance(i, str):
              if not i.isalpha() and i[0] != 'M':
                     list.append(i)
list.sort()
list_array = np.array(list)
# had to change str to float for error bar and standard deviation
new_l = [float(x) for x in list]

# Build the plot
fig = plt.plot()
n, bins, patches = plt.hist(new_l, bins=10, color = 'lightgrey', edgecolor = 'grey')
y, bin_edges = np.histogram(new_l, bins=10)
bin_centers = 0.5*(bin_edges[1:] + bin_edges[:-1])

# calculating the standard deviation of new_l
al_std = np.std(new_l, dtype= np.float64)

plt.errorbar(bin_centers, y, xerr = al_std)


# Save the figure and show
plt.xticks(bins, rotation = 'vertical')
plt.xlabel('26Al/27Al')
plt.ylabel('count')
plt.title('All CAI, CO3 Chondrites')
plt.tight_layout()
plt.show()

######################################################
#scatter plot
# chon = data.loc[data['type'] == 'CO3.0']
# x = chon["26Al/27Al"]
# list = []
# for i in x:
#        if isinstance(i, str):
#               if not i.isalpha() and i[0] != 'M':
#                      list.append(i)
# list.sort()
# list_array = np.array(list)
#
# y = chon["type"]
# y_list = []
# for i in y:
#        if isinstance(i, str):
#               if not i.isalpha() and i[0] != 'M':
#                      y_list.append(i)
# y_array = np.array(y_list)
# print(y_array.shape)
# print(list_array.shape)

#new_y = [item for item in y if not(pd.isnull(item))==True]
# y_list = []
# for i in y:
#        if isinstance(i, str):
#               if not i.isalpha() and i[0] != 'M':
#                      y_list.append(i)
# y_array = np.array(y_list)

# fig = plt.plot()
# plt.scatter(y_array, list_array)
# al_std = np.std(list_array, dtype= np.float64)
# plt.errorbar(y_array, list_array, yerr = al_std)
# plt.show()