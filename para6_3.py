try:
    print("start code")
    print(10/0)
    print("no error")
except (NameError, ZeroDivisionError):
    print("problema ")

print("capsule")