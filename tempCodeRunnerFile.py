n = int(input("Enter the value of n: "))

total = 0

for i in range(2, 2 * n + 1, 2):
    total = total + i

print("Sum =", total)