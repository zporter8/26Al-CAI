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

CO3_0 = data.loc[data['chondrite type'] == 'CO3.0']
c = CO3_0["26Al/27Al"]
l1 = []
for i in c:
    if isinstance(i, str):
        if not i.isalpha() and i[0] != 'M':
            l1.append(i)
l1.sort()
new_l1 = [float(x) for x in l1]

CV3 = data.loc[data['chondrite type'] == 'CV3']
cv = CV3["26Al/27Al"]
l2 = []
for i in cv:
    if isinstance(i, str):
        if not i.isalpha() and i[0] != 'M':
            l2.append(i)
l2.sort()
new_l2 = [float(x) for x in l2]

CM2 = data.loc[data['chondrite type'] == 'CM2']
cm = CM2["26Al/27Al"]
l3 = []
for i in cm:
    if isinstance(i, str):
        if not i.isalpha() and i[0] != 'M':
            l3.append(i)
l3.sort()
new_l3 = [float(x) for x in l3]

CR2 = data.loc[data['chondrite type'] == 'CR2']
cr = CR2["26Al/27Al"]
l4 = []
for i in cr:
    if isinstance(i, str):
        if not i.isalpha() and i[0] != 'M':
            l4.append(i)
l4.sort()
new_l4 = [float(x) for x in l4]


# Create the violin plot
# The white dot in the center of the plot shows the median of the distribution
# The thicker black bar shows the interquartile range of the data
# The thinner black bar shows the data that extends to 1.5 times the interquartile range
# The wider the plot is on a given data point, the more likely a point will fall into the range


fig, (ax1, ax2, ax3, ax4) = plt.subplots(1,4)
sns.violinplot(y=new_l1, palette = 'pastel', ax=ax1)
sns.stripplot(y=new_l1, color='blue', ax=ax1)
ax1.set(xlabel='CO3.0', ylabel='26Al/27Al')
sns.violinplot(y=new_l2, palette = 'pastel', ax=ax2)
sns.stripplot(y=new_l2, color='blue',ax=ax2)
ax2.set(xlabel='CV3')
sns.violinplot(y=new_l3, palette = 'pastel', ax=ax3)
sns.stripplot(y=new_l3, color='blue', ax=ax3)
ax3.set(xlabel='CM2')
sns.violinplot(y=new_l4, palette = 'pastel', ax=ax4)
sns.stripplot(y=new_l4, color='blue',ax=ax4)
ax4.set(xlabel='CR2')
ax1.set_ylim(0,7)
ax2.set_ylim(0,7)
ax3.set_ylim(0,7)
ax4.set_ylim(0,7)


plt.show()