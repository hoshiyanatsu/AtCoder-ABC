#!/usr/bin/env python3

n, k = map(int, input().split())
medicines = [list(map(int, input().split())) for _ in range(n)]
# print(medicines)

day = 0
while True:
    counts = 0
    day += 1
    for i in range(n):
        if medicines[i][0] != 0:
            counts += medicines[i][1]
            medicines[i][0] -= 1
    if counts <= k:
        print(day)
        break
