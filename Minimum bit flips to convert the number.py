start = 3
goal = 4
s_bin = bin(start)[2:]
goal_bin = bin(goal)[2:]
if len(s_bin) > len(goal_bin):
    for i in range(len(s_bin)-len(goal_bin)):
        goal_bin = "0" + goal_bin
else:
    for i in range(len(goal_bin)-len(s_bin)):
        s_bin = "0" + s_bin

print(s_bin)
print(goal_bin)

count = 0

for i in range(len(s_bin)):
    if s_bin[i] != goal_bin[i]:
        count += 1
print(count)