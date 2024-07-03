# writing lists and strings
# jeffrey smith

# create the average of 20 numbers

#list = []
#for i in range(20):
#    num = eval(input("Please enter a number: "))
#    list.append(num)
#print("You entered: ", list)
#print("average", sum(list)/len(list))

#2
def mangle(str):
    str = str.upper()
    str = str[0:2] + str[2:-2] + str[-2:]
    return str

def count_e(list):
    num_e = 0
    for string in list:
         num_e += string.upper().count("E")
    return num_e

def main():
    test_input = ["hellothere", "42 degrees celsius", "eeeeeeee"]
    test_output = ["HELLOTHERE", "42 DEGREES CELSIUS", "EEEEEEE"]
    for i in range(len(test_input)):
        print("Mangle", test_input[i] +":", mangle(test_input[i]) == test_output[i])

        print(count_e(["hi", "hello", "EEK!"]))
        print("count_e", count_e(["hi", "hello", "EEK!"]) == 3)

main()