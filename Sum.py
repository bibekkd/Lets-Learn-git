x = int(input("Enter a number :"))
fac = 1
for i in range(x+1):
    if i == 0:
        continue
    fac *= i

print(f"Factorial of {x} is {fac}.")