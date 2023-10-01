#!/usr/bin/env python3

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum = 0
for i in range(m):
    sum += A[B[i]-1]
print(sum)