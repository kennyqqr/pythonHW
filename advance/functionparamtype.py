"""
assign int type to parameter 'num'
""" 
def num_add_one(num:int):
    print(num+1)
 
"""
1. assign int type to parameter 'num'
2. return type is set to str
"""
def num_add_two_and_return(num:int) -> str:
    return str(num+2)

# no return value
num_add_one(3)
# return a str
n = num_add_two_and_return(4)
print(type(n))
print(n)
