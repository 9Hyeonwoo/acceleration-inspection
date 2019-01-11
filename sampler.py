import sys

if (len(sys.argv) < 2):
    print("give file name")
    sys.exit(0)

try:
    f = open(sys.argv[1], "r")
except Exception:
    print("cant open file")
    sys.exit(0)

lines = f.readlines()
count = 0
for line in lines:
    count += 1
    if (count % 3 == 1):
        print(line, end="")
