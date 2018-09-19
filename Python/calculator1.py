# Python calculator
# Molly and Alex
a = int(input("Enter first number:"))
b = int(input("Enter another number:"))

def doMath(a,b,op):
    if op == 1:
        return str (a+b)
    if op == 2:
        return str (a-b)
    if op == 3:
        return str (a*b)
    if op == 4:
        return str (a/b)
    if op == 5:
        return str (a%b)



print("Sum:\t\t" + doMath(a,b,1))
print("Difference:\t" + doMath(a,b,2))
print("Product:\t" + doMath(a,b,3))
print("Quotient:\t" + doMath(a,b,4))
print("Modulo:\t\t" + doMath(a,b,5))
