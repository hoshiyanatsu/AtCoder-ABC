#!/usr/bin/env python3
N, X = map(int, input().split())
P = list(map(int, input().split()))

for k in range(N):
    if P[k] == X:
        print(k+1)