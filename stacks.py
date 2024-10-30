import queue
import stacks




def flip(stack):
    flipped = stack()
    while not stack.isempty():
        flipped.push(stack.pop())
    return flipped


