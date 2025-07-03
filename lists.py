#Example List
fruits = ['apple','banana','cherry']
print(fruits)

#list operations

#Accessing elements

print(fruits[0])
print(fruits[-1])

#Changing Values
fruits[1] = 'blueberry'
print(fruits)

# Adding Items

fruits.append("orange")
fruits.insert(1, 'kiwi')
print(fruits)

#Removing Items
fruits.remove("apple")
fruits.pop()
del fruits[0]
print(fruits)

#Looping Through a list
for fruit in fruits:
    print(fruit)

#List Length 
print(len(fruits))
