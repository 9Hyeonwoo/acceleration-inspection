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
    # splt[0] is millisceonds
    # splt[1] is x
    # splt[2] is y
    # splt[3] is z

    splt = line.split(", ")

    x = float(splt[1])
    y = float(splt[2])
    z = float(splt[3])
    scala = math.sqrt(x*x+y*y+z*z)
    print(splt[0] + ", " + str(scala))
 
