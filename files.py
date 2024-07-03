# practice with files and dictionaries
#jeffrey smith

letters = ["A", "B", "C", "D", "F"]
counts = {}
file = "letter-grades.txt"

for line in open(file):
    letter = line.replace("\n", "")
    # if commas, use split
    # print(line) # testing
    # get the count of letter if it exists, 0 otherwise
    count = counts.get(letter, 0)
    counts[letter] = count + 1

print("Letter counts: ")
for l in letters:
    print(l +":", counts.get(l, 0))
print()

# print dictionary
print("File grade counts:")
for item in counts.keys():
    print(item + ":", counts[item])


