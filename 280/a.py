#!/usr/bin/env python3
H, W = map(int, input().split())
S = [input() for i in range(H)]
count = 0
for i in range(H):
    for j in range(len(S[i])):
        if S[i][j] == '#':
            count += 1
print(count)
