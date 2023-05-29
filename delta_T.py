import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/f-jorge/f-jorge.github.io/main/Al26_CAIs_data%20-%2026Al_27Al.csv"
data = pd.read_csv(url, index_col=0)

# created a function to calculate the dT
def delta_T(a):
    #print("The time difference between time = 0, and when this CAI formed:")
    return (1.03e6)*(np.log((5.2)/a))

# creating a list of the d26Mg data and removing any words from the dataset
m = data["del26Mg*"]
mg = []
for i in mg:
    if isinstance(i, str):
        # if i[0] != 'M':
        if not i.isalpha() and i[0] != 'M':
            mg.append(i)
mg.sort()
# want floats?
new_mg = [float(x) for x in mg]
print(new_mg)

x = data["26Al/27Al"]
l = []
for i in x:
    if isinstance(i, str):
        # if i[0] != 'M':
        if not i.isalpha() and i[0] != 'M':
            l.append(i)
l.sort()
new_l = [float(x) for x in l]
#print(new_l)

# trying to filter out the negative values bc can't take log of negative?
def check_positive(number):
    if number > 0:
        return True
    return False

positive = filter(check_positive, new_l)
al26_positive = list(positive)
#print(n_positive)

# creating a list of deltaT values from the equation and the filtered al26 values
i = 0
new_deltaT = []
while i < len(al26_positive):
    t = delta_T(al26_positive[i])
    new_deltaT.append(t)
    i = i + 1
#print(new_deltaT)


# creating the plot with del26Mg on x and deltaT on y
# want to have del26Mg on x and both delta T and al26 on y
fig, ax = plt.subplots()
ax.plot(m, new_deltaT)
ax.set_xlim(0,7)
ax.set_xlabel("26Al/27Al")
ax.set_ylabel("time between t=0 and CAI formation (myr)")
#plt.tight_layout()
#plt.savefig("deltaT.png")

# trying to place al26 on y axis as well... on same plot
ax2 = ax.twinx()
ax2.plot(m, al26_positive, color="red")
ax2.set_ylabel('26Al/27Al')
ax2.tick_params(axis='y')

plt.show()




