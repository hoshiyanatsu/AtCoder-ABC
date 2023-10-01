#!/usr/bin/env python3
n, m = map(int, input().split())
s = input()
c = list(map(int, input().split()))
p = [[] for _ in range(m + 1)]
t = ["" for _ in range(n)]
for idx in range(n):
    p[c[idx]].append(idx)
for i in range(1, m + 1):
    k = len(p[i])
    for j in range(k):
        # あまりで出すことによって、indexが 0 のときも適切に対応できるようになってる。if文使わないキレイだね
        t[p[i][(j + 1) % k]] = s[p[i][j]]
print("".join(t))
