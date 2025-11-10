#exceptions

#runtime errors

a=int(input("enter a number"))
b=int(input("enter a number"))

try:
    div=a/b
    print(div)
#except:
#    print("do not put 0")
#except:
#   b=b+0.0001
#    div=a/b
#    print(div)
except ZeroDivisionError:
    print("dont enter 0")
except NameError:
    print("use another number")
except:
    print("error")
#finally:
#    print("executed")
else:
    print("program executed")
