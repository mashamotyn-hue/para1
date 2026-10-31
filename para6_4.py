try:
    print("start code")
    print(10/0)
    print("no error")
except (NameError, ZeroDivisionError) as little_error:
    print(little_error)

print("capsule")
# print(10/0)




