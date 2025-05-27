"""
Problem:  Create a program that determines how many blocks are left over after building the tallest possible valid structure.
    Input:  (y)integer, total number of available blocks
    Output:  (y)integer, leftover blocks
    Rules
        Explicit
            - building blocks are cubes
            - structure is built in layers
            - top layer is a single block
            - each block must be supported by 4 blocks below
            - each block may support more than 1 block
            - gaps are not allow between blocks
        Implicit
            - (y)bottom-layer blocks are supported by 'ground'
            - (y)cubes are all the same size
            - (y)structure is a pyramid
            - (+)a block 'supports' another block if it's touching and below (must be surface contact)
    Questions
        - Check ?s (+)
        - Will there always be blocks leftover? (no)
        - Does each block, besides the top block, need to support at least 1 block? (yes)

Examples/ Test Cases
    print(calculate_leftover_blocks(0) == 0)  # True
    print(calculate_leftover_blocks(1) == 0)  # True
    print(calculate_leftover_blocks(2) == 1)  # True
    print(calculate_leftover_blocks(4) == 3)  # True
    print(calculate_leftover_blocks(5) == 0)  # True
    print(calculate_leftover_blocks(6) == 1)  # True
    print(calculate_leftover_blocks(14) == 0) # True

    - There won't always be blocks left over.
    - Inputs and outputs are all integers.
    - Test cases indicate that the structure is pyramidal.
    - Cubes are all the same size
    - Bottom cubes are supported by 'ground'

    # Blocks 1 → 4 → 9 → 16 → 25 → 36 → 14 → 35
    # Sum    1   5   14  30   55   91   105  150
    print(calculate_leftover_blocks(105) == 14) # True

Data Structures
    -skip

Algorithm
    leftover (int) is the difference between the input and total that can be used in a 'valid structure'.
        Total number in valid structure
            iterate, subtracting the next layers' blocks from input number until the difference is negative
                E.g. num = 16
                    LOOP
                    test_num = num - num_iteration**2
                    # 15
                    # 11
                    # 2
                    # -14
                    if test_num < 0 exit loop and return num # Else continue loop
                    num is set to value of test_num

Code
    - Use a `while True:` loop, and break out of the loop using the return keyword when test_num < 0.
"""
def calculate_leftover_blocks(num):
    iteration = 1
    while True:
        test_num = num - iteration**2
        if test_num < 0:
            return num
        else:
            num = test_num
            iteration += 1


print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
print(calculate_leftover_blocks(105) == 14) # True
print(calculate_leftover_blocks(1000) == 181) # True
print(calculate_leftover_blocks(4900) == 0) # True