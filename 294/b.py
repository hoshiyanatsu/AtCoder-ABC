#!/usr/bin/env python3
alpa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
h, w = map(int, input().split())
A = ['' for _ in range(h)]
for i in range(h):
    A[i] = list(map(int, input().split()))

for i in range(h):
    for j in range(w):
        if A[i][j] == 0:
            print('.', end='')
        else:
            print(alpa[A[i][j]-1], end='')
    print()