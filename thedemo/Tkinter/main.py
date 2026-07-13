import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack() # to show up the label on the screen


# Many positional Arguments
def add(*args):
    print(args[1])

    sum=0
    for n in args:
        sum += n
    return sum

print(add(2,3,4,5,6,7,8,9))


def calculate(**kwargs):
    print(kwargs)
    print(kwargs["add"])
    for key, value in kwargs.items():
        print(key, value)

calculate(add=3, multiply=4)



class Car:
    def __init__(self, **kwargs): # can put any number of argumnets as you want
        self.name = kwargs.get("name") # when you don't give anything while creating object it does not give error instead it returns none
        self.price = kwargs["price"] # when you don't give anything while creating object it gives error

car1 = Car(price=10)
print(car1.name)










window.mainloop()
