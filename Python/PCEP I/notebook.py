'''# Counter Loops
counter = 1
while counter < 11:
	print(counter)
	counter += 1
print	('finished')

# Counter Loops
for counter in range (1, 11):
	print(counter)
print('Finished!')

# For Loop
for letter in 'hello!':
	print('Current letter:', letter)

# While Loops and Breaks
while True:
	name = input('Enter your name or EXIT to close the program: ')
	if (name == 'EXIT'):
		break
	print('Hello', name)

# Continue Loops
for i in range(1, 21):
	if i % 5 == 0:
		continue
	print(i)'''

# Example of a nested loop
'''
for a in range(1, 6):
	for b in range(1, 6):
		print(a, 'x', b, '=', a * b)
'''

#Iterating lists
"""top_cities = ['New york City', 'Los Angeles', 'Chicago', 'Houston',
'Phoenix']
for city in top_cities:
	print('Current city:', city)"""

#Iterating with length
'''top_cities = ['New york City', 'Los Angeles', 'Chicago', 'Houston',
'Phoenix']
for city_index in range(len(top_cities)):
	print('Current index:', city_index, '| Current city:', top_cities[city_index], )'''

# Quick spending loop adition shit
'''spendings = [12321, 18.32, 43223.23, 2342.5, 234.3, 10]
sum = 0.0
for spending in spendings:
	sum += spending
	print('Total money spent:', sum)'''

# Using 'in  and 'not in'.
'''benson_birthday = ['Jojo', 'Sam', 'Skillar', 'Mr.Beast', 'Cristiano Ronaldo']
guest = input('What is your name?')
if guest in benson_birthday:
	print('Welcome to the party!')
else:
	print('No invited, try next year.')'''

# in complex datatyps the name of the list is the name of the data location where the data is stored. 
# Using a slice [:] copies the content without linking the lists
'''initial_list = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
modified_list = initial_list[:]
initial_list[0] = 'one'
print ('The initial list is: ', initial_list, '\nThe modified list is ', modified_list)'''

# List Comprehensions
# An alternative to the first block of code is to compact everything into one line as shown in the second block
'''numbers = []
for i in range(1, 101):
	numbers.append(i)
print(numbers)'''

'''numbers = [i for i in range(1, 101)]
print(numbers)'''

# Nested lists 
'''cells = [['one', 'two', 'three'], ['uno', 'dos', 'tres']]
for x in cells:
	print('Element: ', x)'''

# Uses of cells
'''table = [['one', 'two', 'three'], ['uno', 'dos', 'tres']]
for row in table:
	for cell in row:
		print('Element: ', cell)'''

#Mixing lists
'''list_us = ['New York City', 'Chicago']
list_uk = ['London', 'Bristol']
list_all = list_uk + list_us
print(list_all)'''

#Repeating content within a list
'''list_numbers = [0,1] * 10
print(list_numbers)'''

#Capitalizing stuff
'''text = 'please capitalise me'
text_cap = text.upper()
print(text_cap)'''

# More practice
'''connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]

# Initialize the variables in order to keep track
counter = 0
sum = 0.0

# Iterate through the list 
for flight in connections:
	if flight[1] == 'Rome':
		counter += 1
		sum += flight[2]

print(counter, 'connections lead to Rome with an average flight time of', sum/counter, 'minutes')'''

'''# Dictionaries
grades = {}
grades['Santiago'] = 'B-'
grades['Annie'] = 'A'
grades['Annie'] = 'A+'
print(grades)
if 'Santiago' in grades:
	print('Santiago got a ', grades['Santiago'], 'grade letter')
del grades['Santiago']
grades['Santiago'] = 'B+'

# Printing the elements
for names in grades:
	print(names)

# Printing the keys
for names in grades.keys():
	print(names)

# Printing the values
for names in grades.values():
	print(names)

# Printing the items
for names in grades.items():
	print(names)
'''
# Example of definition
'''def greet():
	print('Hello, my dear!')'''

# Another example
def get_average(input_numbers):
	sum = 0.0
	for number in input_numbers:
		sum += number
	average = sum / len(input_numbers)
	print(average)

get_average([5.0,3.0,5.67,5.3,6.3,2.4])