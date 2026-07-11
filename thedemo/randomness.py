import random
import my_module


print(''' 

 
                  _
                 )_ `.
                )_ `. \\
               )_ `. `|
              )_ `.` /
             )_ `-.` |
            )_ `-.` ` \\
             )_.- ` `  \\
              )_.-` `   \\
               )_.-`\\ /\\ \\
                )_.-| \\O  \\
                    |  \\   \\
          _        /   /    \\        _
         ) `-._   / /O\\  /O\\ \\   _.-` (
        )      `-/  `-'  `-'  \\-`      (
        )     _.-|    __      |-._     (
         )_.-`   \\ .-'  `-._  /   `-._(
                  \\ `-.__.--`/
                   `-._  _.-"
                       ``

 ''')

print('Welcome to the world of randomness!\n The fate is being decided by randomness!!!!!'.upper())

random_integer = random.randint(1,10)
print(random_integer)

print(f'my modules number is:  {my_module.my_module_number}')

print('----'*30)

friends = ['Alice', 'Bob', 'Charlie', 'David','Lucy','Alex','John', 'Tim','Peter']
print(f'Let\'s put on the fate to decide who will be the chosen one : \n{random.choice(friends)}')

# method 2
random_index= random.randint(0,8)
print(friends[random_index])