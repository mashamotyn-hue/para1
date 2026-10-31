try:
    try:
        print("start code")
        print(error)
        print("no error")
    except SyntaxError:
        print("wrong sintax")
except NameError as error:
    print(error)