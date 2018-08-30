#Quadratic solver
#Molly and Alex

print ("Quadratic solver")
print ("Enter the coefficients for ax^2 + bx + c = 0")
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

def doQuad(a,b,c):
    d = (b*b - 4*a*c)
    if d < 0:
        return ("No real roots")
    else:
        myArray = [str((-b + (b**2 - 4*a*c)**.5)/(2*a)), str((-b - (b**2 - 4*a*c)**.5)/(2*a))]
        return myArray
    
returnArray = doQuad(a,b,c)
print(returnArray)
