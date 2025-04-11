# Use the sqrt function from the math library to write some code that outputs the square root of 37. Try to write the code in three different ways.
# ↓ First way to code this.
import math
print(math.sqrt(37))

# ↓ Second way to code this.
import math as m
result = m.sqrt(37)
print(result)

# ↓ Third way to code this.
from math import sqrt
num = 37
result = sqrt(num)
print(result)