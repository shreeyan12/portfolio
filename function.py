#basic syntax
def greet():
    print("Hello, welcome to Day 4!")

greet()  # call the function

#function with parameters

def greet(name):
    print("Hello", name)

greet("Shreeyan")

#function with return value

def add(a, b):
    return a + b

result = add(5, 3)
print("Sum is:", result)


# list in python

fruits = ['apple', 'banana', 'cherry']

print(fruits[-1])
print(fruits[0])

#modify list

fruits.append('orange')     # add item
fruits.remove('banana')     # remove item
print(len(fruits))          # number of items

#loop through a list

for fruit in fruits:
    print(fruit)
