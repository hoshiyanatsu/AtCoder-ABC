#!/usr/bin/env python3

N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))

B = A[0:P-1] + A[R-1:S] + A[Q:R-1] + A[P-1:Q] + A[S:]

for num in B:
    print(num, end=" ")
print()