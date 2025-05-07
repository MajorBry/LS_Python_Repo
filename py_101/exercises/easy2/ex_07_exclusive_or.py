def xor(operand1, operand2):
    return bool((operand1 or operand2) and not (operand1 and operand2))

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)
