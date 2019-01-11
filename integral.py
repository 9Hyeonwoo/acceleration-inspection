from scipy.interpolate import InterpolatedUnivariateSpline as ius
import numpy as np
import sys

if (len(sys.argv) < 2):
    print("give file name to be integrated")
    sys.exit(0)

try:
    af = open(sys.argv[1], "r")
except Exception:
    print("cant open file")
    sys.exit(0)

alines = af.readlines()
acc_start = float((alines[0].split(", "))[0])
acc_end = float((alines[(len(alines)-1)].split(", "))[0])
print(acc_start)
print(acc_end)
ax = []
ay = []

pre_l = 0 
for line in alines:
    parsed = line.split(", ")
    time = float(parsed[0])
    if (pre_l == time):
        pre_l = time
        continue
    ax.append((time - acc_start)/1000)
    ay.append(float(parsed[1])) 
    pre_l = time

for i in range(0,len(ax)-1):
    if ax[i] >= ax[i+1]:
        print("{} is bigger than {}".format(ax[i], ax[i+1]))

acc_x = np.array(ax)
acc_y = np.array(ay)

print(acc_x)
afun = ius(acc_x, acc_y, k=1)

print("acc integral : {}".format(afun.integral(0, (acc_end - acc_start)/1000)))
print(acc_end - acc_start)
