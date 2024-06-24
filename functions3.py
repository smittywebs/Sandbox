# is even function
# Jeffrey Smith

# write a function to tell if a number is even or odd

def is_even(num):
    return num % 2 ==0

def calculate_total(meal, tax_rate, tip_rate):
    tip = meal * tip_rate
    tax = meal * tax_rate
    return meal + tip + tax

def hey(num):
    return num ** 2

def there(num):
    if num < 0:
        return 0
    # else is optional!
    return 2 ** num

def are_we(num, string):
    for i in range(num):
        print("Are we", string, "yet? ", end=" ")
    print()


def main():
    print("4 is even: ", is_even(4))
    print("5 is even: ", is_even(5))
    print("Total should be $66.85", calculate_total(53.48, .07, .18))
    print("hey(5)", hey(5) == 25)
    print("hey(0)", hey(0) == 0)
    print("there(5)", there(5) == 32)
    print("there(0)", there(0) == 1)
    print("there(3)", there(3) == 8)
    print("there(-2)", there(-2) == 0)
    print("there(-6)", there(-6) == 0)
    print('are_we(2, "there")')
    are_we(2,"there")
    print('are_we(3, "50")')
    are_we(3,"50")
    print('are_we(1, "")')
    are_we(1,"")
    print('are_we(0, "hey!")')
    are_we(0,"hey!")


main()

# Calculate total meal
# Jeffrey Smith

#def calculate_total(meal, tax_rate, tip_rate):
#    meal = int(input("Please enter the cost of the meal: "))
#    tip_amount = meal * tip_rate
#    meal_pre_tax = meal + tip_amount
#    tax_amount = meal_pre_tax * tax_rate
#    total_cost = meal_pre_tax + tax_amount
#
#    return total_cost
#
#total = calculate_total(53.48, 0.07, .20)
#print(f"The cost of your meal is: ${total: .2f}")
    
    


