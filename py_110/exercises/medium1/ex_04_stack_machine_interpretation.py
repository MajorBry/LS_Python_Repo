"""
Problem:  create a stack-and-register program
    Input:  string, of commands
    Output:  print
    Rules
        Explicit
            - all operations are integer operations
            - assume all arguments are valid programs
            - initialize the stack to []
            - initialize the register to 0
            - Commands to include:
                	+ n:  Place an integer value, n, in the register. Do not modify the stack.
                    + PUSH:  Push the current register value onto the stack. Leave the value in the register.
                    + ADD:  Pop a value from the stack and add it to the register value, storing the result in the register.
                    + SUB:  Pop a value from the stack and subtract it from the register value, storing the result in the register.
                    + MULT:  Pop a value from the stack and multiply it by the register value, storing the result in the register.
                    + DIV:  Pop a value from the stack and divide the register value by the popped stack value, storing the integer result back in the register.
                    + REMAINDER:  Pop a value from the stack and divide the register value by the popped stack value, storing the integer remainder of the division back in the register.
                    + POP:  Remove the topmost item from the stack and place it in the register.
                PRINT : Print the register value.
        Implicit
            - numbers in string are placed in the register
            - (?)stack and register values are reset for each minilang() function call
    Questions
        - ()

Examples/ Test Cases
↓ See below ↓

Data Structures:  

Algorithm
    - 

Implementation by Code
    - 
"""
def minilang(string):
    stack = []
    register = 0

    tokens = string.split()
    for token in tokens:
        try:
            match token:
                case 'PUSH':
                    stack.append(register)
                case 'ADD':
                    register += stack.pop()
                case 'SUB':
                    register -= stack.pop()
                case 'MULT':
                    register *= stack.pop()
                case 'DIV':
                    register //= stack.pop()
                case 'REMAINDER':
                    register %= stack.pop()
                case 'POP':
                    register = stack.pop()
                case 'PRINT':
                    print(register)
                case _: # ↓ default case assumes integer
                    register = int(token)
        except IndexError:
            return (f"EmptyStack Error: '{token}' token command cannot execute on empty stack")
        except ValueError:
            return (f"InvalidToken Error: '{token}' is invalid")


minilang('PRINT')
# 0
minilang('5 PUSH 3 MULT PRINT')
# 15
minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8
minilang('5 PUSH POP PRINT')
# 5
minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7
minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6
minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12
minilang('-3 PUSH 5 SUB PRINT')
# 8
minilang('6 PUSH')
# (nothing is printed)

print(minilang('6 PUSH ADD PRINT SUB'))
# (EmptyStack Error)

print(minilang('6 PUNCH 7 PRINT'))
# (InvalidToken Error)