# exceptions

# runtime errors


a=int(input("Enter a number"))

b=int(input("Enter a number"))

try:
    print(a/b)
#except:
#    print("Error catch")
#except:
#    b=b+0.0001
#    print(a/b)
except ZeroDivisionError:
    print("denomenator cannot be zero")
else:
    print("Executed with out error")
finally:
    print("Program completed")

