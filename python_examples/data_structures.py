# making a list using list comprehension
# same as
#   a = [0, 1, 4, 9, ..., 16]
a = [x**2 for x in range(5)]
print a
print len(a) # length of the list

# appending to the end of the list
a.append(5**2)
print a

# removing the last element
a.pop()
print a

# taking the first 3 elements
print a[:3]

# taking the last 2 elements
print a[-2:]

# taking the middle 3 elements (a[1], a[2], a[3])
#   NOTE: a[4] is not included!
print a[1:4]

b = [1, 2, 3, 4, 5]
a += b # appending a list
print a

# dictionary is a collection of key-value pairs
d = {'jack': 4098, 'sape': 4139}
d['guido'] = 4127
print d
print d['jack']

# iterating over a dictionary.
for key, value in d.items():
    print key,value

# making an empty dictionary
empty_dict = dict()
