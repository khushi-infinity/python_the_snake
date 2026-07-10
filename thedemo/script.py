print("Hello World!")
print("This will go\nnew line yo!")

# string concatenation
print("Hello" + " is it space")

# Enter your name
firstname = input("What is your name? \n")
print(len(firstname))
# print(len(input("your name?")))

print("Hello "+ firstname)
print("Hello "+input("What is your full name? \n") + "!")

#  what's your type?
print(type("Hello"))
print(type(1234))
print(type(12.34))

# Type casting
print(type(int("342")))
# int(), float(), str(), bool()

# float and int
type(6/3) # float
type(6//3) # int

# power
type(2**2)

#  round
print(round(34.765, 2))

# a different format to print
score = 24
print(f"Your score is: {score}")

print(int("345"))

if score > 100:
    print("You got the trick")
elif score <100 & score > 90:      # and or not
    print("You many be go tthe trick")
else :
    print("you didn't")