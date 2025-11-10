#loops

#for loops,while loops

#for loops

#a=[1,2,3]

#range():to loop a code at a specified number of times
'''
for i in range(1,100):#1,2,3,4,5,6......99
    print(i)

for i in range(50,100):#initial value=0
    print(i)

'''

#543

#3

#123---3
'''
a=int(input("enter the number"))
print(a%10)
'''
# +,-,*,/,//,%

#print(542%10)
'''
a=int(input("enter number"))

if a%2==0:
    print(a,"is even")
else:
    print("odd")

'''

#write a program to print even numbers bw the range 100 to 200
'''
for i in range(100,201):#100,101,102
    if i%2==0:#even
        print(i)


for i in range(100,201,2):#start,stop,step
    print(i)



for i in range(50,0,-1):
    print(i)

'''

#write a program to print numbers which are divisible by 11 bot not by 2
#bw the range 1 to 100
'''
for i in range(1,101):
    if i%11==0 and i%2!=0:
        print(i)



#write a program to find the sum of first 10 natural numbers

sum=0
for i in range(1,11):#1
    sum+=i#sum=sum+1=1,1+2=3,3+3=6
print(sum)


#1+2+3+......+10=55

#1*2*3.....*10=

pro=1
for i in range(1,11):#1
    pro*=i
print(pro)

'''














