
#list

fruits = ["apple", "banana", "mango"]
print(fruits)

#display list item
print(fruits[0])   # apple
print(fruits[2])   # mango


#add item to list
fruits.append("orange")
print(fruits)   # ['apple', 'banana', 'mango', 'orange']

#change item in list
fruits[1] = "grape"
print(fruits)   # ['apple', 'grape', 'mango', 'orange']

#remove item from list
fruits.remove("mango")
print(fruits)   # ['apple', 'grape', 'orange']

#PART 2 — DICTIONARIES
#dictionary

person = {
    "name": "Thamal",
    "age": 27,
    "city": "Colombo"
}

print(person)
print(person["name"])

#add item to dictionary
person["goal"] = "Become an AI Engineer"
print(person)

#change item in dictionary
person["age"] = 28
print(person)

#remove item from dictionary
del person["city"]
print(person)


#PART 3 — LOOPS

numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)

#LOOP THROUGH DICTIONARY
for key, value in person.items():
    print(key, ":", value)


#LOOP USING RANGE
for i in range(1, 6):
    print("Number:", i)


