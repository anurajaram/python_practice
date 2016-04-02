# Author = Anupama Rajaram
# Description = function to calculate basic geometric formulae
#             Calculate area and circumference of a circle, given radiu = r 

# Definition of radius
r = 0.43

# Import the math package
import math as m

# Calculate circumference 'C'
C = 2*(m.pi)*r

# Calculate area 'A'
A = (m.pi)*(r**2)

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))
