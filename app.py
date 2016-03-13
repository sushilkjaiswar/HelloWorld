"""
The add function does addition of two numbers and return the
resuts in integer format.
e.g.
   3 + 5 = 8
"""


def add(a, b):
    if is_number(a) and is_number(b):
        return a + b
    return False

"""
The following is_number checks if the argument passed is numeric
then says its true or says false.
e.g.
  is_number("ff") == False not a number
  is_number(2) == True a number
"""


def is_number(a):
    try:
        float(a)
        return True
    except ValueError:
        return False
