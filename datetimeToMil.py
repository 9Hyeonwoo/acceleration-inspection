from datetime import datetime as dt
import sys
import math

try:
    if (len(sys.argv) > 1):
        f = open(sys.argv[1], "r") 
    else:
        print("give file name")
        sys.exit(0)
except Exception:
    print("Wrong Path")
    sys.exit(0)

lines = f.readlines()

for line in lines:
     
    splt = line.split(", ")
    timeStamp = splt[0]
    tmp = dt.strptime(timeStamp, "%Y-%m-%dT%H:%M:%S.%fZ")
    mil = int(tmp.timestamp() * 1000)
    
    print(str(mil), end="") # for location_acc
    for i in range(0, len(splt)):
        if i == 0:
            continue
        print(', ' + splt[i], end="") # concat line
