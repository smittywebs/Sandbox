file = open("turing.txt")
lines = []
for line in file:
    lines.append(line.rstrip())
file.close()
print(lines[:2])
print(lines[-2:])
