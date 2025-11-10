# string : collection of characters
# immutable : cannot changeble after creating


# len() : count of collections


'''
name="Amjath hassan"
print(len(name))

name="amjath hassan"
print(name.title())
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.count("a"))
print(name.swapcase())

# indexed
print(name[0])
print(name.find("n")) # return index position
print(name.split())
print(name.split("a"))
print(name.capitalize().isalpha())
print(name.isdigit())


print(name[0:2]) # slicing
print(name[::-1])
print(name[-1])

for i in name:
    print(i)

del name  # deleting 
print(name)
'''


# List 

# mutable, [], indexed, hetergenous (can store single type elements)
# duplicates can be stored

'''

lst=[1,2,3,4,5, "a", "b"]
print(len(lst))
lst.append("Amjath")
print(lst)
print(lst.extend((1,2)))
print(lst)


for i in lst:
    print(i)

lst.insert(1,"Hassan")
print(lst)

lst.remove("a")
print(lst)

lst.pop(1)
print(lst)
lstn=[1,2,3,4,5]
lst.reverse()
print(lst)

lstn.sort()
print(lstn)

lstn.sort(reverse=True)
print(lstn)

print(max(lstn))
'''


# Tuple
# immutable
# ()
# heterogeneous
# duplication alowed
# indexed

'''
tpl=(1,2,3, "Amjath", "Hassan")

for i in tpl:
    print(i)


c_lst=list(tpl)
c_lst.append(10)
tpl=tuple(c_lst)
print(tpl)


print(tpl[0])

#unpacking
a, b, c = (10, 20, 30)
print(a)

del tpl

t1=(1, 2, 3)
t2=(4, 5, 6)
print(t1+t2)
'''











































