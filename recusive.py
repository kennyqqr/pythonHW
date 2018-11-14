# sample from w3school.com
# https://www.w3schools.com/python/python_for_loops.asp
def tri_recursion(k):
    if(k>0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(5)