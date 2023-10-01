#!/usr/bin/env python3
# from collections import OrderedDict
n, q = map(int, input().split())

# p_1 = 1
# not_go = []

events = [input() for _ in range(q)]

# for ev in events:
#     if ev == '1':
#         not_go.append(p_1)
#         p_1 += 1
#     elif ev == '3':
#         print(not_go[0])
#     else:
#         x = int(ev.split()[1])
#         not_go.remove(x)
# 理解できてない
ans = 1
gone = [None] * (n+1)

for ev in events:
    if ev == '1':
        continue
    elif ev == '3':
        while gone[ans]:
            ans += 1
        print(ans)
    else:
        x = int(ev.split()[1])
        gone[x] = 1