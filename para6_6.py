def checker(var1):
    if type(var1) != str:
        raise TypeError(f"sorry we can`t` work with {type(var1)}, we need str type")
    else:
        return var1
    
f_var = "text"
s_var = 10
checker(f_var)
checker(s_var)
