#dictionary

#{}
#mutable
#ordered
#duplicates not allowed
#key-value pair

person={"name":"sona","age":30,"phone":87654321}
print(person)

print(person.keys())

print(person.values())

print(len(person))

print(person.get("name"))

#print(person.pop("age"))

#print(person.popitem())
'''
person.update({"adress":"abbgftvu"})

print(person)

for i in person:
    print(i)

for i in person.items():
    print(i)

for i in person.values():
    print(i)
'''
#set

#{}

#unordered
#duplication not allowed

s={1,2,3,4,5,5,5}
print(s)

print(len(s))


s.add(10)

s.discard(2)
s.remove(1)
print(s)

x={"a","b",1,2}
y={"a","b",3,4}

#x.symmetric_difference_update(y)

x.intersection_update(y)

print(x)

l=[1,2,3,3,2,4,5,6,6,7,8]

a=set(l)

b=list(a)

print(b)
























