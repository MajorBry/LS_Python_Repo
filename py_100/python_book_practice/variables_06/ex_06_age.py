# Write a program named age.py that includes someone's age and then calculates and reports the future age 10, 20, 30, and 40 years from now. Here's the output for someone who is 22 years old.
# Copy Code
# You are 22 years old.
# In 10 years, you will be 32 years old.
# In 20 years, you will be 42 years old.
# In 30 years, you will be 52 years old.
# In 40 years, you will be 62 years old.
AGE = 22

print(f'You are {AGE} years old.')
for i in range(10,50,10):
    print(f'In {i} years, you will be {AGE + i} years old.')
