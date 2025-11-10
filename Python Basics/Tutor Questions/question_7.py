# Tuple questions.
#
#
# 1. Write a program to find the length of a tuple (1,2,3,9,10) without using len function.

t=(1,2,3,9,10)
l=0
for i in t:
    l+=1
print(l)

# 2. Add an element 200 to the above tuple ( convert the tuple into a list,then add)
list(t).append(100)
print(tuple(t))


# 3. (1,2,3....10).find the largest and smallest elements of this tuple.

t=(1,2,3,4,5,6,7,8,9,10)
print(min(t), max(t))

# 4. Slice only (1,2,3,4)

print(t[:4])

# 5. Print the elements 8,6 from the tuple.

print(t[7], t[5])

# 6. Given a tuple t = (1, 2, 3, 2, 4, 2, 5), count how many times 2 appears.

t = (1, 2, 3, 2, 4, 2, 5)
c=0
for i in t:
    if i ==2:
        c+=1
print(c)

# 7. Write a program to check if an element 2 exists in a tuple.

if 2 in t:
    print(2 , " in ", t)