import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#


#def reverse_array(arr):
#    # Initialize two pointers
#    start = 0
#    end = len(arr) - 1
#    
#    # Swap elements using the two pointers
#    while start < end:
#        # Swap elements at start and end indices
#        arr[start], arr[end] = arr[end], arr[start]
#        # Move pointers towards the center
#        start += 1
#        end -= 1
#
## Example usage:
#if __name__ == "__main__":
#    # Input array of integers
#    array = [1, 4, 3, 2]
#    
#    # Reverse the array in place
#    reverse_array(array)
#    
#    # Print reversed array
#print(array)

name = input("What is your name? ")
print("Hello " + name)
length = len(name)
print(length)
