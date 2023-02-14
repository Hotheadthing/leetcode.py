deck = [17,13,11,2,3,5,7]
# deck = [1,2,3]
arr = []

while len(deck) != 0:
    if len(arr) == 0:
        arr.append(deck[-1])
        deck.pop()
    else:
        while deck[-1] < arr[-1]:
            arr.append(deck[-1])
            deck.pop()
            if len(deck) == 0:
                break
        if len(deck) != 0:
            temp = deck.pop()
            while arr[-1] < temp:
                deck.append(arr[-1])
                arr.pop()
                if len(arr) == 0:
                    break
            arr.append(temp)


print(arr)
result = []
