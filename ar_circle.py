#Define a function to calculate the area of a circle using the formula.
import math
def arr_circle(r):
    area = (math.pi)*(r**2)
    return area
a = float(input("Enter the radius of the circle : "))
print("Area of the circle is : ",arr_circle(a))
