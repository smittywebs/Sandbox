# read file
# jeffrey smith

dataFile = open("add2.txt")

for line in dataFile:
    print(f"{"-"} {line.rstrip()}")
dataFile.close()


