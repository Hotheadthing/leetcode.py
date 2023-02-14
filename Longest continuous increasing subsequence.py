nums = [1,3,5,4,7]
nums = [2,2,2,2,2]
m_count = 1
c_count = 1

for i in range(len(nums)-1):
    if nums[i+1] > nums[i]:
        c_count += 1
    else:
        m_count = max(c_count,m_count)
        c_count = 0
print(m_count)
