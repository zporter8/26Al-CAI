import numpy as np

def delta_T(a):
    print("The time difference between time = 0, and when this CAI formed:")
    return (1.03e6)*(np.log((5.2e-5)/a))

test = delta_T(.98)
print(test)