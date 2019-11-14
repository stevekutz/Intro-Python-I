print("Hello, world!")

# declaring a variable
# ensure that your variable names follow convention
# use snake_case
# CAPS_CASE is usually for constant variables (even though they are the same as normal vars)
name = 'Austen'

print(name)
# string concatenation
print("Hello " + name)

# f-strings
print(f'Hello, {name}')

# create a list with some numbers
q = [10, 60, 20, 5]

# add an element to q
print(q)
q.append(77)
# q now hass 77 at the end
print(q)

# print all values in each list
for element in q:
    print(element)

# using list comprehensions...
numbers = [1, 2, 3, 4, 5]
# create a new list containing the squares of all values in `numbers`
# loop over each number in numbers
    # take each number, and just n * n
    # add to new list
squares = [num**2 for num in numbers]
print(numbers)
print(squares)

# create a new list containing only the even values of `numbers`
evens = [num for num in numbers if num % 2 == 0]
print(evens)

# create a new list containing only the names that start with 
# `s` so that they are properly capitalized 
# (regardless of how the name originally appears) 
names = ["Sarah", "jorge", "sam", "frank", "bob", "sandy", "shawn"]
s_names = [name.capitalize() for name in names if name[0].lower() == 's']
print(s_names)

# create an empty dictionary
d = {}

# create a dictionary with at least two key : value pairs
d = {
    'apple': 'is a fruit',
    'cucumber': 'is a vegetable'
}


# # access & print an element in the dictionary
print(d['apple'])
# re-assign a value
d['apple'] = 'is the best fruit'
print(d)
# # iterate through dictionary
# d.items returns a list of tuples
print(d.items())

for key, value in d.items():
    print(f'{key}: {value}')

for pair in d.items():
    print(f'{pair[0]}: {pair[1]}')


# sets 
fruits = {'apple', 'banana', 'cherry'}
print(fruits)
fruits.add('tomato')
fruits.add('apple')
print(fruits)
# how to check if an item is in a set
print('banana' in fruits)

for fruit in fruits:
    print(fruit)

# tuple
animals = ('dog', 'cat', 'moose', 'beaver')
print(animals)
print(animals[0])

for animal in animals:
    print(animal)

single_tuple_str = ('one')
single_tuple = ('one',)

print(type(single_tuple))
print(single_tuple)
print(len(single_tuple))