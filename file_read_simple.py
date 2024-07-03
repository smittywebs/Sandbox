# simple file read
# jeffrey smith

dataFile = open("add.txt")

for line in dataFile:
    print(line.rstrip())
dataFile.close()