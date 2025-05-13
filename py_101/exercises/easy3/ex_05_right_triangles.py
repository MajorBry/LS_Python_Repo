def triangle(n):
    for j in range(1, n + 1):
        print(' ' * (n - j), '*' * j, sep='')

for num in range(1,11):
    triangle(num)
