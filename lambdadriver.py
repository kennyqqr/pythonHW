x = lambda a : a + 11
y = lambda a,b: a * b
z = lambda a,b,c: a*a + b*b == c*c

print(x(3))
print(y(2,4))
print(z(3,4,5))


def powerfun(n):
    return lambda a : a ** n

mydoubler = powerfun(2)

print("16 * 16 = " + str(mydoubler(16)))