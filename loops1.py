# writing loops 1
# Jeffrey Smith

#1a

for i in range(1,6):
    print(i)
print()

#1b

for i in range(2,12, 3):
    print(i)
print()

#1c

for i in range(-10,1, 2):
    print(i, end=" ")
print()

#1d

for i in range(4):
    print("*" * 4)
print()

for i in range(4): # lines
    for j in range(4): # columns for each row
        print("*", end="")
    print()

#2

for c in "csci 150":
    print(c)
print()

#3

for i in range(1,11, 1):
    print(i)
print()