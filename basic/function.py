def no_arg():
    a = "uccu"
    b = 1.5
    #call function 1
    with_arg(a)
    with_default_value_arg(a)
    with_default_value_arg()
    print(power_num(b))

def with_arg(a):
    print("the input is " + a)

def with_default_value_arg(a="XV"):
    print("arg = "+a)

def power_num(b):
    return b*b

no_arg()