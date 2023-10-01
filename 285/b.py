#!/usr/bin/env python3

N = int(input())
S = list(input())
l = 0

for i in range(1, N):
    l = N-i
    for k in range(1, l+1):
        if S[k-1] == S[k+i-1]:
            l = k-1
            break
    
    print(l)