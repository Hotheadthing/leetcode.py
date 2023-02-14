timeSeries = [1,4]
duration = 2
# timeSeries = [1,2]
# duration = 2
nMap ={}

for i in range(len(timeSeries)):
    for j in range(timeSeries[i],timeSeries[i]+duration):
        if j not in nMap:
            nMap.__setitem__(j,1)

print(len(nMap))
