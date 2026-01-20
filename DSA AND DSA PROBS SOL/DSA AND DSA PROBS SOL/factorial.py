#iterative
n = 5
fact = 1
for i in range(1, n + 1): 
    fact *=  i
print((fact))

# recursive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)