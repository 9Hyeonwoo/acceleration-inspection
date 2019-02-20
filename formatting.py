import sys
import math

if (len(sys.argv) != 3):
    print("plz type [acceleration file], [location fil]")    
    sys.exit(0)
else:
    try:
        af = open(sys.argv[1], 'r')
        lf = open(sys.argv[2], 'r')
    except Exception:
        print("cant open file")
        sys.exit(0)

alines = af.readlines()
llines = lf.readlines()

firstAccTime = int((alines[0].split(", "))[0])
locIndex = 0
targetLocationTime = 0
targetSpeed = 0
targetTimeNext = 0

groupIndex = 0
groupTime = firstAccTime

while(locIndex < len(llines) - 1):
    parsed = llines[locIndex].split(", ")
    parsedNext = llines[locIndex+1].split(", ")
    locTime = int(parsed[0])
    locTimeNext = int(parsedNext[0])
    if (locTimeNext - firstAccTime < 0):
        locIndex += 1
        continue
    else:
        targetLocationTime = locTime
        targetSpeed = float(parsed[2])
        targetTimeNext = locTimeNext
        break

for line in alines:
    accParsed = line.split(", ")
    accTime = int(accParsed[0])
    x = float(accParsed[1])
    y = float(accParsed[2])
    z = float(accParsed[3])
    scala = math.sqrt(x*x + y*y + z*z)
    if accTime - groupTime > 3000:
        groupIndex += 1

    groupTime = accTime

    if targetTimeNext < accTime:
        while(locIndex < len(llines) - 1):
            parsed = llines[locIndex].split(", ")
            parsedNext = llines[locIndex+1].split(", ")
            locTime = int(parsed[0])
            locTimeNext = int(parsedNext[0])
            if (locTimeNext < accTime):
                locIndex += 1
                continue
            else:
                targetLocationTime = locTime
                targetSpeed = float(parsed[2])
                targetTimeNext = locTimeNext
                break

    print(str(groupIndex)+","+accParsed[0]+","+str(x)+","+str(y)+","+str(z)+","+str(scala)+","+str(targetLocationTime)+","+str(targetSpeed))
    
        
