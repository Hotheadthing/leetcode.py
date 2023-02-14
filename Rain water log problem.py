# nums = [0,1,0,2,1,0,1,3,2,1,2,1]
nums = [0,1,0,2,1,0,1,3,2,1,2,1]
empty_cell = [0,1,0,2,1,0,1,3,2,1,2,1]
variable = 0

for i in range(len(nums)):
    if nums[i] > variable:
        variable = nums[i]
    else:
        nums[i] = variable
print(nums)

for j in range(len(empty_cell)-1,-1,-1):
    if empty_cell[j] > variable:
        variable = empty_cell[j]
    else:
        empty_cell[j] = variable
print(empty_cell)
