# List Comprehension

# new_list = [new_item for item in list]

numbers = [1,2,3,4,5]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

name = "Computer"
letter_list = [letter for letter in name]
print(letter_list)


range_list = [n*2 for n in range(1,5)]
print(range_list)


# Conditional List Comprehension
# new_list = [new_item for item in list if test]
names = ['Alex', 'John', 'Timmy', 'Bob', 'Peter Parker', 'Johnson']
short_names = [name for name in names if len(name)<5]
print(short_names)

upper_names = [name.upper() for name in names if len(name)>5]
print(upper_names)