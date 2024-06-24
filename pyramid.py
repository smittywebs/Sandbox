# pyramid prctice
# Jeffrey Smith

def pyramid(char, number):
    for i in range(1, number + 1):
        print(char * i)

def absolute_difference(num1, num2):
    diff = abs(num1 - num2)
    return diff

def main():
    print("difference 5 10", absolute_difference(5, 10) == 5)
    print("difference 10 5", absolute_difference(10, 5) == 5)
    print("difference 200 -200", absolute_difference(200, -200) == 400)
    print()

    print('pyramid("*", 2)')
    pyramid("*", 2)
    print()

    print('pyramid("*", 5)')
    pyramid("+", 5)
    print()

    print('pyramid("x", 10)')
    pyramid("x", 10)
    print()

main()