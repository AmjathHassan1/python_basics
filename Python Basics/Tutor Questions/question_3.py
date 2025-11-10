# For loops questions

# 1 .Write a program to print odd numbers between 1000 and 2000

# start=1000
# end=200
#
# for i in range (start, end+1):
#     if i % 2 != 0:
#         print(i)
#     i+=1

# ========================================================================

# 2 . Write a program to print numbers which are divisible by both 2 and 3 bw the range 1 to 100

# start=1
# end=100
#
# for i in range(start,end+1):
#     if i%2==0 and i%3==0:
#         print(i)


# ========================================================================

# 3. Find the sum of first 20 even numbers

# start=1
# sum=0
# count=0
# for i in range(start,100):
#     if i%2==0:
#         sum=sum+i
#         count=count+1
#         if count==20:
#             break
# print(sum)

# ===================================================

# 4. Find the product of numbers bw 1 and 100

# start=1
# prd=1
# for i in range(start,101):
#     prd*=i
# print(prd)

# ===================================================

# 5. Write a program to find the sum of multiples of 5 bw the range 1 to 50

# start=1
# end=50
# sum=0
# for i in range(start,end+1):
#     if i%5==0:
#         sum+=i
# print(sum)

#===============================================
# 6. Find the factorial of a number input by the user.
#  Eg :input :5  Output=120

# num=int(input("Enter a number: "))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(fact)


# ===================================================

#7 . Write a program to find the count of even numbers bw 1050 and 1200

# start=1050
# end=1200
# count=0
# for i in range(start,end+1):
#     if(i%2==0):
#         count+=1
# print(count)

# =====================================================================


# 8 . Write a program to find the count of both even and odd numbers bw 1 to 50

# start=1
# end=50
# odd=0
# even=0
# for i in range(start,end+1):
#     if(i%2==0):
#         even+=1
#     else:
#         odd+=1
# print(odd)
# print(even)

# ===================================================

# 9. Create a multiplication table using for loop input by the user
# Eg : input :5


# num=int(input("Enter a number: "))
# for i in range(1,11):
#     print(num,"*",i,"=",num*i)

# ===================================================


# 10. Write a program to print the first 20 numbers and their squares using for loop.

# start=1
# end=20
# for i in range(start,end+1):
#     print(i, i**2)

# ===================================================

# 11. Print the series 1000, 2000, 3000, 4000, 5000

# start= 1000
# diff=1000
# end=5000
# for start in range(start,end+1, diff):
#     print(start)
#     start+=diff

# ===================================================

# 12. Print numbers bw 2000 and 1500 in reverse order

# start=1500
# end=2000
# for i in range(end-1,start, -1):
#     print(i)

# ===================================================

# 13. Print numbers from 1 to 10, but stop the loop when you find a number divisible by 7

# start=1
# end=10
# for i in range(start,end+1):
#     print(i)
#     if(i%7==0):
#         break
#     print(i)


# ===================================================

# 14. Print numbers from 1 to 10 but skip 5.

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)

# ===================================================

# 15. Print all numbers from 1 to 10 except multiples of 3.


# for i in range(1, 11):
#     if(i % 3 == 0):
#         continue
#     print(i)