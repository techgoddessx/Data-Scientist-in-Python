print('a' + 'b')
print('a' + ' ' + 'b')
print('This' + 'is' + 'a' + 'sentence.')
print('This' + ' ' + 'is' + ' ' + 'a' + ' ' + 'sentence.')

# Joining two or more strings together like this is known as concatenation.

# We can also repeat a string several times by using the * operator, followed by a number. The number tells Python how many times to repeat the string:

print('a' * 1)  # This will output: a
print('a' * 4) # This will output: aaaa

print('a ' * 5) # This will output: a a a a a
print('a' * 0) # No output for this line
print('a' * -1) # No output for this line

# However, we need to be careful when trying to combine strings with numbers. Python doesn't allow us to do this directly. For example, the following will not work:

# print('4' + 1)  # This will give an error print('4' - 1.0)


