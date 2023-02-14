letters = ["c","f","j"]
target = "a"
letters = ["c","f","j"]
target = "c"
letters = ["c","f","j"]
target = "d"

for i in range(len(letters)):
    if ord(letters[i]) > ord(target):
        print(letters[i])
        break
