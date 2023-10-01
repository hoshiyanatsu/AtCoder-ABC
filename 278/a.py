#!/usr/bin/env python3
N, K = map(int, input().split())
A = list(map(int, input().split()))

for i in range(K):
    A = A[1:]
    A.append(0)
print(*A)