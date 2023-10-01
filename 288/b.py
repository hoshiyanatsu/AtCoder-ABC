#!/usr/bin/env python3

N, K = map(int, input().split())
names = []
for i in range(N):
    names.append(str(input()))

ans = names[0:K]
ans.sort()
for name in ans:
    print(name)