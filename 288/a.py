#!/usr/bin/env python3

N = int(input())
C = []
ans = []
for i in range(N):
    C.append(list(map(int, input().split())))

for i in range(N):
    ans.append(C[i][0] + C[i][1])

for num in ans:
    print(num)