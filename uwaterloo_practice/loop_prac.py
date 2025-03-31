# time = 5
# while time > 0:
#     print(time)
#     time = time - 1
# print('Blastoff!')

# for counter in range(0,22,3):
#     print("Hi " + str(counter))

# n=0
# while n < 10:
#     print(n)
#     if n == 4:
#         n = 10
#         continue
#     n += 1

# Factorization of input
n = int(input())
for x in range(1,n+1):
   if n % x == 0:
      print(str(x), 'times', str(int(n / x)), 'equals', str(n))