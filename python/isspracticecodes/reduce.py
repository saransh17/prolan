from functools import reduce

initial = int(input("Enter the initial : "))

def do_sum(x1, x2): return x1 * x2

def calcsumsquaers(a,b): return a*a+b*b

print(reduce(do_sum, [1, 2, 3, 4,initial]))
print(reduce(calcsumsquaers, [1,2,3]))