def greet(name): # parameter
    print(f'Hello {name}')

greet("Cherry") # argument


programming_dictionary = {
'a':1,
'b':2,
'c':3,
}

print(programming_dictionary['a'])

programming_dictionary['d'] = 4
print(programming_dictionary)

# nested list in dictionary
fruits = {
    'favourite' : ['Apple', 'Mango', 'Banana'],
    'normal' : ['grapes','orange','watermelon']
}

print(fruits['normal'])
print(fruits['favourite'][1])

nested_list = ['A', 'B', ['C','D']]
print(nested_list)
print(nested_list[2])
print(nested_list[2][1])