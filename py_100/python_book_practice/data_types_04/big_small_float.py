import sys
# The maximum number of digits that can be accurately presented
print(sys.float_info.dig)          # Typically 15
# The largest possible positive float value
print(sys.float_info.max)          # About 1.8 * (10**308)
# The smallest non-zero positive float value
print(sys.float_info.min)          # About 2.2 * (10**-308)