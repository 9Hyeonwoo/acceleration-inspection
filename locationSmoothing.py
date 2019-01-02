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

pre_time = -1
pre_speed = -1

ma_size = 6
count = 0
ma_array = [0] * ma_size

for line in lines:
    # splt[0] is mili sceond
    # splt[2] is for speed

    splt = line.split(", ")
    mil = int(splt[0])

    if count < ma_size:
        ma_array[count] = float(splt[2])
        count += 1

    ave_speed = 0
    for i in range(0, ma_size):
        ave_speed += ma_array[i]
    ave_speed /= ma_size
   
    if (pre_time == -1):
        pre_time = mil
        pre_speed = ave_speed
        continue

    delta_time = (mil - pre_time) / 1000
    delta_speed = ave_speed - pre_speed
    
    if (delta_time <= 0):
        continue
    
    acc = delta_speed / delta_time   
    print(str(mil) + ", " + str(ave_speed) + ", " + str(acc))
    
    pre_time = mil
    pre_speed = ave_speed

    for i in range(0, ma_size-1):
        ma_array[i] = ma_array[i+1]
    ma_array[ma_size-1] = float(splt[2])

