import math

# Welcome messages
print("Calculating the roots of a quadratic equation.")
print("If there is only one solution, it will be returned as an integer.")
print("If there are two solutions, it will be returned as a tuple.")
print("If there are no roots, None will be returned")
print("Equations must be in the form of => Ax^2 + Bx + C = 0")

a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))

# Roots will be calculated inside the function
def rootcalculator(a, b, c):
    # By root I mean ==> b^2 - 4ac
    root = b**2 - (4 * a * c)

    # When there are two solutions
    if root > 0:
        # The roots
        x1 = ((-b) + math.sqrt(root)) / (2 * a)
        x2 = ((-b) - math.sqrt(root)) / (2 * a)
        
        # Returning both roots as a single tuple
        return (x1, x2)
    
    # There is only one solution
    elif root == 0:
        return -b / (2 * a)
    
    # No solution
    else:
        return None

# Printing the results
print(rootcalculator(a, b, c))
