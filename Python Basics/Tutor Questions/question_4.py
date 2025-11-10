# While loops questions
#
# 1. Write a program  to print even numbers between 100 and 200 using while

# start=101
# end=200
# while start < end:
#     if  start % 2==0:
#         print(start)
#     start = start + 1

# =======================================================

# 2. Write a program to print the sum of first 100 natural numbers using while

# num=1
# sum=0
# while num<=100:
#     sum+=num
#     num+=1
# print(sum)

# =============================================

# 3. Find the factorial of a number using while

# num=int(input("Enter a number: "))
# factorial=1
# start=1
# while start<=num:
#     factorial=factorial*start
#     start=start+1
# print(factorial)

# ===============================================

# 4. Write a program to generate multiplication table using while

# num=int(input("Enter a number: "))
# start=1
# while start<=10:
#     print(num, " * ", start, " = ",num * start)
#     start=start+1

# ===============================================

# 5. Write a program to print first 50 even numbers in reverse order

# start=100
# count=0
# while start>0:
#     if start%2==0:
#         print("The number is even", start)
#         count=count+1
#
#     start=start-1
# print("The number count", count)

# 6. Count the even numbers bw the range 5 and 105

# start=5
# end=105
# while start <= end:
#     if start%2==0:
#         print(start)
#     start=start+1

# =====================================================

# 7. Count both even and odd numbers bw the range 100 and 300

# start=101
# end=300
# odd=0
# even=0
# while start < end:
#     if start%2==0:
#         even+=1
#     else:
#         odd+=1
#     start=start+1
#
# print("odd count:",odd)
# print("even count:",even)

# =============================================

# 8. Print the series 5000,4000,3000,2000,1000

# start=5000
# while start>=1000:
#     print(start)
#     start-=1000

# =================================================

# 9. Write a program to find the count of digits in a number

# num=int(input("Enter a number: "))
# count=0
# while num>0:
#     count=count+1
#     num//=10
# print(count)

# =================================================

# 10. Write a program to find the sum of digits a number input by the user.
#    Eg :input :123
#           Output:1+2+3=6

# num=int(input("Enter a number: "))
# sum=0
# while num>0:
#     sum+=num%10
#     num//=10
# print(sum)


# ==============================================

# 11. Write a program to find the product of digits of a number input by the user.
#   Eg :input :123
#         Output:1*2*3=6(hind:use both floor division and modulus operators)
#

# num=int(input("Enter a number: "))
# prod=1
# while num>0:
#     prod*=num%10
#     num//=10
# print(prod)

# 12. Display all the numbers which are divisible by 5 bw 1 and 100


# i=1
# while i <100:
#     if i % 5 ==0:
#         print(i)
#     i+=1