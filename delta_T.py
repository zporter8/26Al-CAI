import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/f-jorge/f-jorge.github.io/main/Al26_CAIs_data%20-%2026Al_27Al.csv"
data = pd.read_csv(url, index_col=0)

def delta_T(a):
    #print("The time difference between time = 0, and when this CAI formed:")
    return (1.03e6)*(np.log((5.2)/a))

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

def check_positive(number):
    if number > 0:
        return True
    return False

positive = filter(check_positive, new_l)
al26_positive = list(positive)
#print(n_positive)

i = 0
new_deltaT = []
while i < len(al26_positive):
    t = delta_T(al26_positive[i])
    new_deltaT.append(t)
    i = i + 1
#print(new_deltaT)


plt.plot(al26_positive, new_deltaT)
plt.xlim(0,7)
plt.xlabel("26Al/27Al")
plt.ylabel("time difference between t=0 and formation of CAI")
#plt.tight_layout()
#plt.savefig("deltaT.png")
plt.show()




