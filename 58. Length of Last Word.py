s = "   fly me   to   the moon  "
finished = (s.strip(' '))
for i in range(len(finished)-1,-1,-1):
    if finished[i] == ' ':
        break
s = finished[i+1:]
print(len(s))
