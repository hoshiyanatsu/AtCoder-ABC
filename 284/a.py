#!/usr/bin/env python3

N = int(input())
S = []
for i in range(N):
    S.append(str(input()))

for i in range(N):
    print(S[N-i-1])