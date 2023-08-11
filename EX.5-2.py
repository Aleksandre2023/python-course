import math

# Function to calculate the circumference of a circle
def circle_circumference(radius):
    return 2 * math.pi * radius

# Function to calculate the area of a circle
def circle_area(radius):
    return math.pi * radius**2

# Function to calculate the volume of a sphere
def sphere_volume(radius):
    return 4/3 * math.pi * radius**3

# Function to calculate the area of a rectangle
def rectangle_area(x, y):
    return x * y

# Function to calculate the perimeter of a rectangle
def rectangle_perimeter(x, y):
    return 2 * (x + y)

# Testing the functions with different values
radius = 5
x = 4
y = 6

print("Circle Circumference with radius", radius, ":", circle_circumference(radius))
print("Circle Area with radius", radius, ":", circle_area(radius))
print("Sphere Volume with radius", radius, ":", sphere_volume(radius))
print("Rectangle Area with sides", x, "and", y, ":", rectangle_area(x, y))
print("Rectangle Perimeter with sides", x, "and", y, ":", rectangle_perimeter(x, y))
