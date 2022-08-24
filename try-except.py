try:
    a = b
except TypeError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("this is a test")
finally:
    print("it final")
