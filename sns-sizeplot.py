import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/f-jorge/f-jorge.github.io/main/Al26_CAIs_data%20-%2026Al_27Al.csv"
data = pd.read_csv(url, index_col=0)

x = data["26Al/27Al"]
l = []
# reducing the data to only numerical values by removing words
for i in x:
    if isinstance(i, str):
        # if i[0] != 'M':
        if not i.isalpha() and i[0] != 'M':
            l.append(i)
l.sort()
new_l = [float(x) for x in l]

g1 = data["CAI size x"]
g_1 = []
for i in g1:
    if isinstance(i, str):
        if not i.isalpha() and i[0] != 'M':
            g_1.append(i)
g_1.sort()
new_g1 = [float(x) for x in g_1]

# trying to create function to filter the size values we want
def check_small(number):
    if number <= 100:
        return True
    return False
small = filter(check_small, new_g1)
n_small = list(small)
#print(n_small)

def check_medium(number):
    if number > 100 and number <=500:
        return True
    return False
medium = filter(check_medium, new_g1)
n_medium = list(medium)
#print(n_medium)

def check_large(number):
    if number > 500:
        return True
    return False
large = filter(check_large, new_g1)
n_large = list(large)
#print(n_large)


# we want the al26 ratios on the y axis not the sizes
# this only plots the size
# how to lock the data together?
fig, (ax1, ax2, ax3) = plt.subplots(1,3)
sns.violinplot(y=n_small, palette = 'pastel', ax=ax1)
sns.stripplot(y=n_small, color='blue', ax=ax1)
ax1.set(xlabel='small', ylabel= 'size')
sns.violinplot(y=n_medium, palette = 'pastel', ax=ax2)
sns.stripplot(y=n_medium, color='blue',ax=ax2)
ax2.set(xlabel='medium')
sns.violinplot(y=n_large, palette = 'pastel', ax=ax3)
sns.stripplot(y=n_large, color='blue', ax=ax3)
ax3.set(xlabel='large')
#ax1.set_ylim(0,7)
#ax2.set_ylim(0,7)
#ax3.set_ylim(0,7)

plt.show()