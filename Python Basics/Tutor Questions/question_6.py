# List questions
#
#
# 1. Li=["a","b","c"].given a list of elements and find the length if the list without using len function.

# Li=["a","b","c"]
# len_ = 0
# for letter in Li:
#     len_ += 1
# print(len_)

# 2. Convert all the elements in the list li into uppercase.

# Li=["a","b","c"]
# print(list("".join(Li).upper()))

# 3. Write a program to find the square of each element in the given list [1,2,3,4] and generate a new list contains the squares.

# list_ = [1,2,3,4]
# square_lst = []
# for item in list_:
#     square_lst.append(item ** 2)
# print(square_lst)

# 4. Find the largest and smallest elements from a list.

# list_ = [1,2,3,4]
# print(max(list_), min(list_))


# 5. Find the largest element from a list without using max function.

# list_ = [1,2,3,4]
# max=0
# for i in list_:
#
#     if i>max:
#         max = i
# print(max)

# 6. From a given list [5,6,7] find the factorial if each elements and generate a new list if the factorial.expected output :[120,720,5040].

# l=[5,6,7]
# fl=[]
# for i in l:
#     prd=1
#     for j in range(1,i+1):
#         prd*=j
#     fl.append(prd)
# print(fl)

# 7. From a given list ["hai","hello","welcome"] find the reverse of each element and generate a new list.

# l=["hai","hello","welcome"]
# rl=[]
# for i in l:
#     rl.append(i[::-1])
# print(rl)


# 8. L=[1,2,3,4,5,6,7,8,9,10].sort the list in reverse order.
L=[1,2,3,4,5,6,7,8,9,10]
# L.sort(reverse=True)
# print(L)

# 9. Slice first 4 elements

print(L[:4])

# 10. Slice last 5 elements using negative index.

print(L[-5:])

# 11. Create two empty lists,name=[ ] and age=[ ] .insert names and ages of 3 people into the lists input by the user.expected output:name =["sona","megha","arya"],age=[27,25,21].

# name=[]
# age=[]
# for i in range(3):
#     name.append(input("Enter your name: "))
#     age.append(int(input("Enter your age: ")))
# print(name,age)

# 12. Animals=["cat","dog"]. Add a new element elephant to the list.

Animals=["cat","dog"]
Animals.append("elephant")
print(Animals)

# 13. Insert an element "rat" into the index position 1.
Animals.insert(1, "rat")
print(Animals)

# 14. L=[1,2,3,4,5,6].filter out only even numbers from this list.

L=[1,2,3,4,5,6]
even=[]
for i in L:
    if i%2==0:
        even.append(i)
print(even)

# 15. L=[-2,-7,-8,1,2,4].find the odd number count from the list.

L=[-2,-7,-8,1,2,4]
c=0
for i in L:
    if i%2!=0:
        c+=1
print("count ", c)


# 16. Create a list of multiples of 5 bw the range 1 to 100.output :[5,10,15.....,100].
m_5=[]
for i in range(1,101):
    if i%5==0:
        m_5.append(i)
print(m_5)

# 17. [100,120,140,160].find the sum of elements of this list.

L=[100,120,140,160]
sum=0
for i in L:
    sum+=i
print(sum)