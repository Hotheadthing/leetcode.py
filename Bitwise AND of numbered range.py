left = 5
right = 7
i = 0
print(f"the value of left is {bin(left)[2:]}")
print(f"the value of right is {bin(right)[2:]}")
print(2&4)
while left != right:
    x = bin(right)[2:]
    # print(f"the initial value of left is {x}")
    left = left >> 1
    right = right >> 1
    i += 1
    y = bin(right)[2:]
    # print(f"the after value of left is {y}")

print(bin(left)[2:])
print(bin(i)[2:])
z = left << i
print(bin(z)[2:])