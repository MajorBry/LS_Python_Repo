"""
Problem:  create an is_balanced function that determines whether the parentheses within a string are balanced
    Input:  string
    Output:  bool, True if all balance, false otherwise
    Rules
        Explicit
            - parenthetical pairs must start with (, not )
        Implicit
            - 
    Questions
        - 

Examples/ Test Cases
print(is_balanced("What (is) this?") == True)
print(is_balanced("What is) this?") == False)
print(is_balanced("What (is this?") == False)
print(is_balanced("((What) (is this))?") == True)
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)           
print(is_balanced(")Hey!(") == False)        
print(is_balanced("What ((is))) up(") == False)  

Data Structures:  

Algorithm
    - 

Implementation by Code
    - 
"""
def is_balanced(string):
    open = {'(':0, '{':0, '[':0}
    close = {')':'(', '}':'{', ']':'['}
    for char in string:
        if char in open:
            open[char] += 1
        elif char in close:
            open[close[char]] -= 1
            if open[close[char]] < 0:
                return False
    if tuple(open.values()) != (0, 0, 0):
        return False
    return True


# ↓ All output True
print(is_balanced("(What) {is} [this]?") == True)
print(is_balanced("What is} this?") == False)
print(is_balanced("What {is this?") == False)
print(is_balanced("{[What] {is this}}?") == True)
print(is_balanced("{{What}} {is this}}?") == False)
print(is_balanced("[Hey!]") == True)           
print(is_balanced("}Hey!{") == False)        
print(is_balanced("What {is}]} up{") == False)

# print(is_balanced("What (is) this?") == True)
# print(is_balanced("What is) this?") == False)
# print(is_balanced("What (is this?") == False)
# print(is_balanced("((What) (is this))?") == True)
# print(is_balanced("((What)) (is this))?") == False)
# print(is_balanced("Hey!") == True)           
# print(is_balanced(")Hey!(") == False)        
# print(is_balanced("What ((is))) up(") == False)

