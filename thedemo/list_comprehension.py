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


# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_value:new_value for (key,value) in dict.items()}

import random
student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)
passed_students = {student:score for (student, score) in student_scores.items() if score>=50}
print(passed_students)


# Loops through Dictionary and Dataframe
student_dict = {
    "student" : ["James","Alex","Lilly"],
    "score" : [53,75,96]
}

# loop thorugh dictionary
for (key,value) in student_dict.items():
    print(key)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# loop through data frame
for (key,value) in student_data_frame.items():
    print(key)

# built in method where loops through each of the rows
for (index,row) in student_data_frame.iterrows():
    print(index)