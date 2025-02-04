#Error handling
#interupting normal exeecuting of a code  is called error or exception


#try except

try:
    print("welcome")
except:
    print("error")
else:
    print("no error")
finally:
    print("always")

try:
    print("welcome"  + 123)
except TypeError:
    print("type error")
except ValueError:
    print("value error")
    