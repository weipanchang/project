import math
import sys

# This function may not be completely correct
def rectangle_dimensions(length):
    min_width = int(math.sqrt(length))
    max_height = int(math.ceil(math.sqrt(length)))

    return (min_width, max_height)

def slice(xs, width):
    return [xs[i:i+width] for i in range(0, len(xs), width)]

def patch(s, width):
    if len(s) == width: return s
    else: return s + (" " * (width - len(s)))

# Main function
def square_encode(s):
    w, h = rectangle_dimensions(len(s))
    raw_rectangle = slice(s, h)

    # Last element may not have actual width needed
    fixed_rectangle = raw_rectangle[:-1] + [patch(raw_rectangle[-1], h)]

    """
    The following uses a trick in Python that lets us use lists as arguments
    to arbitrary length functions. Python's zip function takes a variable
    number of arguments, meaning you can pass it 2, 3, 4, etc. arguments. If
    I have a list of lists, I don't know how many internal lists I have, but
    I want to zip them all up. By prefixing the list identifier with a *, I
    can tell the Python interpreter to "unpack" the list and feed them as arguments
    one by one.

    Ex.

    xs = [[1, 2], [3, 4]]
    print zip(*xs) # Prints [(1, 3), (2, 4)]
    """
    encoded = zip(*fixed_rectangle)

    return [''.join(s) for s in encoded]

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("Usage: python %s [sentence]" % sys.argv[0])

    no_spaces = ''.join(sys.argv[1:])
    #print no_spaces
    encoding = square_encode(no_spaces)
    print ' '.join(encoding)
