arriveAlice = "08-15"
leaveAlice = "08-18"
arriveBob = "08-16"
leaveBob = "08-19"
aA = []
lA = []
aB = []
lB = []
days = 0
aA.append(int(arriveAlice[0:2]))
aA.append(int(arriveAlice[3:]))

lA.append(int(leaveAlice[0:2]))
lA.append((int(leaveAlice[3:])))

aB.append(int(arriveBob[0:2]))
aB.append(int(arriveBob[3:]))

lB.append(int(leaveBob[0:2]))
lB.append((int(leaveBob[3:])))

if aB[0] > lA[0]:
    days = days
elif aB[0] == lA[0]:
    if lA[1] > aB[1]:
        days = lA[1] - aB[1]
elif aB[0] < lA[0]:
    if aA[0] < aB[0]:
        days =



