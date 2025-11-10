# Dictionary questions
#
# 1.create this Dictionary
#
# student = {"name": "Alice", "age": 20, "course": "Data Science"}

student = {"name": "Alice", "age": 20, "course": "Data Science"}


# Update the age to 21.

student["age"] = 21
student.update({"age": 21})

# 2.Add a new key grade with value "A".

student["grade"] = "A"
print(student)


# 3.marks = {"Math": 90, "Science": 85, "English": 88}

# Print all the keys

marks = {"Math": 90, "Science": 85, "English": 88}
dict_keys = list(marks.keys())
for key in dict_keys:
    print(key, marks[key])

# 4.Print only the subjects (keys) where marks are greater than 85.

for key in dict_keys:
    if marks[key] > 85:
        print(key, marks[key])


# 5.create a dictionary from two lists

# keys = ["name", "age", "city"]
# values = ["John", 25, "Delhi"]

keys = ["name", "age", "city"]
values = ["John", 25, "Delhi"]

d=dict()
for i in range(len(keys)):
    d[keys[i]] = values[i]
print(d)
dt=zip(keys, values)
dt=dict(dt)
print(dt)

# 6.Create a dictionary with keys as numbers from 1 to 5 and values as their cubes.

d={}
for i in range(1, 5):
    d[i] = i*i
print(d)



# 7.marks = {"Math": 90, "Science": 85, "English": 88}
# Write a program to find the product of all values in a dictionary.

marks = {"Math": 90, "Science": 85, "English": 88}
prd=1
for key, value in marks.items():
    prd*=value
print(prd)


# 8.remove the last pair from the above dictionary.

marks.popitem()
print(marks)
#
# Set questions
#
# 1.Create a set of fruits and check if "apple" is present in it.

fruits = {"apple", "banana", "orange"}
print(fruits)

# 2.Add a new element to a set using the add() method.

fruits.add("cherry")
print(fruits)

# 3.Remove an element from a set using remove() and discard().

fruits.discard("cherry")
fruits.remove("orange")
print(fruits)

# 4.Find the length of a set.

print(len(fruits))

# 5.Delete an entire set using del.

del fruits

# 6.convert a set into a list and print them

fruits = {"apple", "banana", "orange"}
fruits=list(fruits)
for fruit in fruits:
    print(fruit)

# 7.A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
#
# Find the difference (A-B)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.difference(B))

# 8.find intersection
print(A.intersection(B))
# 9.find symmetric difference
print(A.symmetric_difference(B))

# 10.Create a set and use a loop to find the sum of all elements.
s={1,2,4,5}
sum=0
for i in s:
    sum+=i
print(sum)