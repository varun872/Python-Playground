str1="hello welcome"
print(str1[0:4]) #string slicing(starting number is included whereas ending number is not included)
print(str1[0:]) #full string is printed
print(len(str1)) #prints the length of the srting(number of characters)
'''
Syntax:
[start:stop:step]
step=by default is 1
step is basically tells by how much to skip
'''
#Cheeky way to reverse a string is to use negative string slicing [::-1]

#String Functions
print(str1.count('e'))
print(str1.find('come'))
print(str1.replace('come','go'))
print(str1.upper())
print(str1.isalpha())

# str.split() turns a string into a list of smaller strings, breaking on whitespace by default.
# str.join() takes us in the other direction, sewing a list of strings up into one long string, using the string it was called on as separator
# .format() on a "format string", where the Python values we want to insert are represented with {} placeholders.
