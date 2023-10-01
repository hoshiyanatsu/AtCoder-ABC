#!/usr/bin/env python3

n = int(input())
X = input().split()
i = 0
for w in X:
    X[i] = int(w)
    i += 1

X = sorted(X)

for _ in range(n):
    X.pop(0)
for _ in range(n):
    X.pop(-1)

sum = 0

for num in X:
    sum += num
print(sum/(3*n))