def triangle(a, b, c): # ← a, b, and c are integer angles of the triangle in degrees
    angles = [a, b, c]
    if sum(angles) != 180 or a <= 0 or b <= 0 or c <= 0:
        return 'invalid'
    if 90 in angles:
        return 'right'
    for angle in angles:
        if angle > 90:
            return 'obtuse'
    return 'acute'

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True
