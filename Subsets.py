nums = [1,2,3]
nums = [3,2,4,1]
res = [[]]
for num in nums:
    length = len(res)
    # print(f"the lenght of res is {length}")
    for i in range(length):
        res.append(res[i] + [num])
        # print(f"the valu of res is {res}")

# print(res)
print(2^3)
print(bin(7)[2:])
