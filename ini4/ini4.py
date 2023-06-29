a = int(input("a: "))
b = int(input("b: "))
nums = []
n = a
for i in range(a, b):
    if n % 2 != 0:
        nums.append(n)
    n = n + 1
if b % 2 != 0:
    nums.append(b)
print(sum(nums))