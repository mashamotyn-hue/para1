   def checker(func, *args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as exc:
            print(f" we have promeblem {exc}")
        else:print(f"no pronvblernm. ROESULT = {result}")


    def calculate(expression):
        return eval(expression)
calculate('2+2')