def double(x):
    return 2 * x

def quad(x):
    return double(double(x))

def hello(name):
    print("Hello", name + ", how are you today?")

def repeat(string, n):
    return string * n

def square(string, n):
    for i in range(n):
        print(repeat(string, n))

print(double(5))
print(quad(4))
hello("Jeff")
print(repeat("hi", 10))
square("*", 4)