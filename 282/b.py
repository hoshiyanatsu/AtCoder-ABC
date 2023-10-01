#!/usr/bin/env python3

N, M = map(int, input().split())
S = []
counter = 0

for i in range(N):
    S.append(str(input()))

for i in range(N):
    for k in range(i+1, N):
        for j in range(M):
            if S[i][j] == S[k][j] == 'x':
                break
            elif j == M-1:
                counter += 1
                break
print(counter)