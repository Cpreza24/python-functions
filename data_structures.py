favorite_animal = 'dog'

student = {
    'name': 'Maria',
    'favorite_integer': 5,
    favorite_animal: 'llama' # notice the lack of quotes around favorite_animal
}

print(student)
# prints: {'name': 'Maria', 'favorite_integer': 5, 'dog': 'llama'}
# note the 'dog' key - the value of the favorite_animal variable is used


name = student['name']
print(name)
# prints: Maria


# favorite_food = student['favorite_food']
# error: KeyError: 'favorite_food'

print(student.get('favorite_food'))
# prints: None


if 'course' in student:
    print(f"{student['name']} is enrolled in {student['course']}")
else:
    print(f"{student['name']} is not enrolled in a course")
    # prints: Maria is not enrolled in a course


student['name'] = 'Mariana'
print(student['name'])
# prints: Mariana

student['age'] = 25

del student['dog']
# verify that the item was deleted
print('dog' in student)
# prints: False


print(student)
# prints: {'name': 'Maria', 'favorite_integer': 5, 'age': 25}
print(len(student))
# prints: 3
print(len({}))
# prints: 0

for key in student:
    print(f"{key} is {student[key]}")
    # prints:
    # name is Maria
    # favorite_integer is 5
    # age is 25


for key, val in student.items():
    print(f"{key} is {val}")
    # prints:
    # name is Maria
    # favorite_integer is 5
    # age is 25


for key, val in student.items():
    print(f"{key} is {val}")
    # prints:
    # name is Maria
    # favorite_integer is 5
    # age is 25



where_my_things_are = {
    'pc': 'office',
    'toothbrush': 'bathroom',
    'car': 'garage',
}

for key in where_my_things_are:
    print(f'My {key} is kept in the {where_my_things_are[key]}')

colors = ['red', 'green', 'blue']

colors[-1] = 'brown'
print(colors)
# prints: ['red', 'green', 'brown']

# The JS equivalent to push()
colors.append('purple')
print(colors)
# prints: ['red', 'green', 'brown', 'purple']
# purple was added to the end of the list

colors.extend(['orange', 'black'])
print(colors)
# prints: ['red', 'green', 'brown', 'purple', 'orange', 'black']
# orange and black were added to the end of the list


colors.insert(0, 'yellow')
print(colors)
# prints: ['red', 'yellow', 'green', 'brown', 'purple', 'orange', 'black']
# yellow was added at the 1 index; no elements were replaced


green = colors.pop(2)
print(colors)
# prints: ['red', 'yellow', 'brown', 'purple', 'orange', 'black']
# green was removed at the 2 index and is in the green variable


colors.remove('orange')
print(colors)
# prints: ['red', 'yellow', 'brown', 'purple', 'black']


# colors.clear()
# print(colors)
# # prints: []


colors = ['red', 'green', 'blue']
for color in colors:
    print(color)
    # prints:
    # red
    # green
    # blue

for idx, color in enumerate(colors):
    print(idx, color)
    # prints:
    # 0 red
    # 1 green
    # 2 blue


tupel_colors = ('white', 'purple', 'orange')
print(tupel_colors[1])
# prints: green

for idx, tupel_color in enumerate(tupel_colors):
    print(idx, tupel_color)
    # prints:
    # 0 red
    # 1 green
    # 2 blue



nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []

# we want 'n * n' for each 'n' in nums 
for n in nums:
    squares.append(n * n)

print(squares)
# prints [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
