nums1 = [4,1,2]
nums2 = [1,3,4,2]
nums1 = [1,3,5,2,4]
nums2 = [5,4,3,2,1]
arr = []
for i in range(len(nums1)):
    ind = nums2.index(nums1[i])
    if ind == len(nums2) - 1:
        arr.append(-1)
    else:
        flag = False
        for j in range(ind+1,len(nums2)):
            if nums2[j] > nums1[i]:
                arr.append(nums2[j])
                flag = True
                break

        if flag == False:
            arr.append(-1)

print(arr)

