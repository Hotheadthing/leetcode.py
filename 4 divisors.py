
#Issues



nums = [7286,18704,70773,8224,91675]
nums3 = []
for i in nums:
    if i % 2 == 0:
        nums3.append(i)
    elif i % 3 == 0:
        nums3.append(i)
    else:
        count3 = 0
sum1=0

for j in nums3:
    a=[]
    for i in range(1,j+1):
        # print(i)
        if (j % i) == 0:
            a.append(i)
            # print(i)
    if(len(a)==4):
        sum1=sum1+sum(a)
print(sum1)
#     if j % 3 == 0:
#         factor = j//3
#         if factor == 3 or factor == 1:
#             count = 0
#         elif factor % 2 == 0 or factor % 3 == 0:
#             count =0
#         for i in range(2, factor):
#             # print(i)
#             if (factor % i) == 0:
#                 count = 0
#         else:
#             print("Its a prime")
#         #         count += 1 + 3 + factor + j
#         # print(count)
#                 # count3 += count
#         #     el
#         # elif factor % 2 == 0 or factor %3 == 0:
#         #     count =0
#         # else:
#         #     count += 1+3+factor+j
#         #     count3 += count
#         # print(count)
#     else:
#         factor = j//2
#         if factor ==2 or factor == 1:
#             count2 = 0
#         for i in range(2, factor):
#             if (factor % i) == 0:
#                 count2 += 1 + 3 + factor + j
#                 count3 += count2
#         # elif factor % 2 == 0 or factor % 3 == 0:
#         #     count2 = 0
#         # else:
#         #     count2 += 1 + 2 + factor + j
#         #     count3 += count2
#             # print(count)
#             # count2 = count + count2
#             # print(count2)
#             # print(count2)
#
# # print(f"This is the value of count3:{count3}")
#
# # [7286,18704,70773,8224,91675]
#
#











