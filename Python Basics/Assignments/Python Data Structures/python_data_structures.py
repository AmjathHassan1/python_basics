# Data structures in python

# Topic :List
# Exercise
# Q1. Create a list of 5 random numbers and print the list.

randon_lst=[11, 22, 33, 44, 55]
print("randon number list : ",randon_lst)


# Q2. Insert 3 new values to the list and print the updated list.

new_items=[11,22,33]
updated_lst=randon_lst+new_items
print("randon number list : ",updated_lst)



# Q3. Try to use a for loop to print each element in the list.

for i in range(len(updated_lst)):
    print(updated_lst[i], " in index of ", i)

# Topic: Dictionary
# Exercise
# Q1. Create a dictionary with keys 'name', 'age', and 'address' and values 'John', 25, and 'New York' respectively.


data= {"name": "John", "age": 25, "address": "New York"}

# Q2. Add a new key-value pair to the dictionary created in Q1 with key 'phone' and value '1234567890'.

data["phone"]=1234567890
print(data)


# Topic: Set
# Exercise
# Q1.Create a set with values 1, 2, 3, 4, and 5.

new_set=set([1,2,3,4,5])
print(new_set)

# Q2. Add the value 6 to the set created in Q1.

new_set.add(6)
print(new_set)

# Q3. Remove the value 3 from the set created in Q1.

new_set.discard(3)
print(new_set)


# Topic:Tuple
# Exercise
# Q1. Create a tuple with values 1, 2, 3, and 4

tpl=tuple([1, 2, 3, 4])


# Q2. Print the length of the tuple created in Q1.


print(len(tpl))
