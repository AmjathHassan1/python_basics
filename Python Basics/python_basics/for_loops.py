# loops
# for loops, while loop

# for loo[s
# a = [1,2,3]
# range() : to loop a code at a special number of times
''''''
''
''''''
''
# write a program to print even number 100 to 200

'''
start = 100
end = 200
for num in range(100, 201):
    if num % 2 == 0:
        print(num, " is even number")


for num in range(100, 201): #start , stop, step
    if num % 2 == 0:
        print(num, " is even number")


for i in range(50,0,-1):
    print(i)
'''

# write a program to print number divisible by 11 but
# not by 2 between the range 1 to 100


'''

start = 1
end = 101
for num in range(start, end):
    if num % 11 == 0 and not num % 2 == 0:
        print(num)
'''



#write a programme to find the sum of 10 natty number

'''
sum=0
for num in range(1,11):
    sum+=num

print(sum)

# write a programme to find the product of first 10 
prod=1
for num in range(1,11):
    prod*=num

print(prod)
'''













































