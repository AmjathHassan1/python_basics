#it is used to execute a block of statements repeatedly until a given condition
#is satisfied


#while condition:
    #body of while
'''
while True:
    print("hello")
'''
'''
i=1
while i<=10:
    print("hello")
    i=i+1#1+1=2,2+1=3........10+1=11
'''


#write a program to print odd numbers bw 100 and 200
'''
i=100
while i<=200:
    if i%2==1:
        print(i)
    i+=1


i=101
while (i<=200):
    print(i)
    i+=2#100+2=102,102+2=104

'''

#break,continue,pass
'''

for i in range(1,50):
    
    if i==25:
        break
    print(i)


i=1
while (i<50):
    #print(i)
    if i==25:
        break
    print(i)
    i+=1
'''

#continue
'''
for i in range(1,11):
    if i==5:
        continue
    print(i)

i=1
while (i<=10):
    if i==5:
        i+=1
        continue
    print(i)
    i+=1
'''

#pass
for i in range(1,100):
    pass























