# If the strings contain characters that form a valid number (like '4', '3.3', '12', etc.), it's possible to convert them to integers or floats first, and then do the arithmetical operations. We can use the int() or float() function to convert a string of type str to a number of type int or float.

print(int('4') + 1)
print(float('3.3') + 1)

# print(int('wrong format')) won't work

# Notice that while the addition of the integers printed the sum of a and b, when converted into a string by the str() function it printed the concatenation of the strings instead. 

a = 2
b = 5

print(a+b)
print(str(a)+str(b))
