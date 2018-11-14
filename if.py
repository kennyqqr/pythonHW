a = 78
b = 87

if a == b:
    print("a equals b")
elif a < b:
    print("a less than b")
else:
    print("a greater than b")

print("a: I am higher") if a > b else print("a: I am smaller")
print("A") if a > b else print("=") if a == b else print("B") # output is B

