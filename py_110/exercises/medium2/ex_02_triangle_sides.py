"""
Problem:  make a function that determines what kind of triangle is made given 3 side lengths
    Input:  3 numbers, (int or float) side lengths
    Output:  string, triangle classification or invalid
    Rules
        Explicit
            - return 'equilateral' if all three sides have the same length
            - return 'isosceles' if two sides have the same length, while the third is different
            - return 'scalene' if all three sides have different lengths
            - return 'invalid' if the three lengths can't make a triangle
            - lengths can't make a triangle if:
                + one of the lengths is 0, or
                + the sum of the two smallest side lengths isn't greater than the largest side length
        Implicit
            - 
    Questions
        - ()

Examples/ Test Cases
↓ see below ↓

Data Structures:  

Algorithm
    Note: if the longest length is shorter than the sum of the other two sides, then the same is true for another side length; therefore, finding the maximum side length is unnecessary

Implementation by Code
    - 
"""
def is_triangle(a, b, c):
    lengths = [a, b, c]
    if 0 in lengths:
        return False
    for length in lengths:
        if sum(lengths) - length < length:
            return False
    return True

def triangle(a, b, c): # ← a, b, and c are side lengths of the triangle
    lengths = {a, b, c}
    if len(lengths) == 1:
        return 'equilateral'
    if len(lengths) == 2:
        if is_triangle(a, b, c):
            return 'isosceles'
    elif is_triangle(a, b, c):
        return 'scalene'
    return 'invalid'
    

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True