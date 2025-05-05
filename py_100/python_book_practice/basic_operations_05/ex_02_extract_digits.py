# 	2. This question may be a little challenging if your math skills are rusty. Don't be afraid to take advantage of the hints. Try your best to solve the problem, but don't feel compelled to complete it if you become frustrated.
# Use the REPL and the arithmetic operators to extract the individual digits of 4936:
# 		1. One place is 6.
# 		2. Tens place is 3.
# 		3. Hundreds place is 9.
#       4. Thousands place is 4.
number = 4936
print(f'Ones place is {number%10}.')
print(f'Tens place is {(number%100)//10}.')
print(f'Hundreds place is {(number%1000)//100}.')
print(f'Thousands place is {number//1000}.')