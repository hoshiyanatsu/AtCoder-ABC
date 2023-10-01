#!/usr/bin/env python3
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

num_a = 0
num_b = 0
for i in range(n+m):
    if num_a == n:
        B[num_b] = i+1
        num_b += 1
    elif num_b == m:
        A[num_a] = i+1
        num_a += 1
    else:
        if A[num_a] < B[num_b]:
            A[num_a] = i+1
            num_a += 1
        else:
            B[num_b] = i+1
            num_b += 1
for i in range(n):
    print(A[i], end=' ')
print()
for i in range(m):
    print(B[i], end=' ')
print()