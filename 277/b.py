#!/usr/bin/env python3
N = int(input())
S = [input() for i in range(N)]
f = 'HDCS'
s = 'A23456789TJQK'
check = True
for i in range(N):
    if S[i][0] not in f:
        check = False
        break
    elif S[i][1] not in s:
        check = False
        break
    for j in range(i+1, N):
        if S[i] == S[j]:
            check = False
            break
if check:
    print("Yes")
else:
    print("No")