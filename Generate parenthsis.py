n = 3
arr = []
ans = []

def backtracking(op,cl):
    if op == cl == n:
        ans.append("".join(arr))
        print(f"ans is {ans}")
        print(f"arr is {arr}")
        return

    if op < n:
        arr.append("(")
        print(f"opening arr1 {arr}")
        backtracking(op+1,cl)
        arr.pop()
        print(f"opening arr2 {arr}")
    if cl < op:
        arr.append(")")
        print(f"closing arr1 {arr}")
        backtracking(op,cl+1)
        arr.pop()
        print(f"closing arr2 {arr}")

    return ans

print(backtracking(0,0))