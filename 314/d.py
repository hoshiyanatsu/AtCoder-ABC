n = int(input())
li_s = list(input())
q = int(input())
li_t = [list(map(str, input().split())) for _ in range(q)]
henko_s = ["" for _ in range(n)]
komoji = False
omoji = True
for ts in li_t:
    if ts[0] == "1":
        li_s[int(ts[1]) - 1] = ts[2]
    elif ts[0] == "2":
        li_s = [s.lower() for s in li_s]
    elif ts[0] == "3":
        li_s = [s.upper() for s in li_s]

print("".join(li_s))
