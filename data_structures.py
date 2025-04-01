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