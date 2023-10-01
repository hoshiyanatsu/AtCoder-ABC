#!/usr/bin/env python3

n = int(input())
As = [list(map(str, input())) for _ in range(n)]


result = [[0] * n for _ in range(n)]

for i in range(n - 1):
    result[0][i + 1] = As[0][i]
for i in range(n - 1):
    result[i + 1][n - 1] = As[i][n - 1]
for i in range(n - 1):
    result[n - 1][i] = As[n - 1][i + 1]
for i in range(n - 1):
    result[i][0] = As[i + 1][0]

for j in range(n - 2):
    for k in range(n - 2):
        result[j + 1][k + 1] = As[j + 1][k + 1]

for i in range(n):
    for j in range(n):
        print(result[i][j], end="")
    print()
