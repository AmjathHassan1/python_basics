# disctionary

# {}
# mutable
# ordered
#duplicates not allowed
#ky-value pair

'''
person={'name': "sdf", "age":23, "af":"asdf"}
print(person)

print(person.keys())
print(person.values())
print(len(person))
print(person.get('name'))
print(person.pop('age'))
print(person.popitem()) # removes the last key-value

person.update({"add":"asd"})

print(person)


for i in person:
    print(i)

for i in person.items():
    print(i)

for i in person.values():
    print(i)
'''


# Set

# {}
# unordered
# duplication not allowed

s={1,2,3,4,5}
print(s)
s={1,2,3,4,4,5}
print(s)
print(len(s))


s.add(10)
print(s)

s.discard(2)
print(s)

s.remove(1)
print(s)


x={"a","b",1,2}
y={"a", "b", 3, 4}

print(x,y)

#x.symmetric_difference_update(y) # both diffrence elements returned to x
x.intersection_update(y)


print(x)


l=[1,2,3,3,4,5,5]
l=list(set(l))
print(l)






























