#!/usr/bin/env python3

h, w = map(int, input().split())
A = [input().split() for _ in range(h)]

cnt = 0
for i in range(h):
    for j in range(w):
        A[h-i][w-j]