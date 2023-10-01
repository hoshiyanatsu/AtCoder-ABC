#!/usr/bin/env python3
n, h, x = map(int, input().split())
p = list(map(int, input().split()))

ok = False

for i in range(n):
    kaihuku = h + p[i]
    if kaihuku >= x:
        ok = True
        mininum = i + 1
        break
print(mininum)
