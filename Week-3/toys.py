'''
toys.py

Simple toy functions to get comfortable working 
with functions.
'''


# write a function that adds 1
# to the input and prints the result
def inc(a):
    print(int(a) + 1)
inc(input("enter number: "))


# write a function that adds 1
# to the input and returns the result
def inc_return(a):
    return int(a) + 1
inc(input("enter number: "))  # hint this is incomplete


# write a function that adds
# the two input numbers together
# and returns the sum

def sum(a, b):
    sum = a + b
    return sum
x = int(input("nom 1: "))
y = int(input("nom 2: "))
nom = sum(x, y)

print(nom)



# write a function that takes two
# numbers, adds them together using 
# sum() and then increments the sum
# using inc_return
def sum_inc(a, b):
    sum_inc = a + b + 1
    return sum_inc
x = int(input("nom 1 : "))
y = int(input("nom 2 : "))
nom = sum_inc(x, y)
print(nom)


# write a function that returns a 
# boolean (True or False) for whether 
# the input number is even
def is_even(a):
    if a % 2 == 0:
       return True
    else:
        return False
b = int(input("enter number: "))
ans = is_even(b)
print(ans)


# create for loop that takes a string
# and an integer and returns a new string 
# that is the string repeated equal to 
# integer
# e.g. string_repeat('ho', 3) returns
# 'hohoho'
def string_repeat(phrase, repeat):
    string_repeat = phrase * int(repeat)
    # hint: you can add strings together 
    # in order to concatenate them
    return string_repeat
x = input("gimme a phrase: ")
y = int(input("repeat: "))
ans = string_repeat(x, y)
print(ans)

