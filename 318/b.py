#!/usr/bin/env python3

xys = ["" for _ in range(10201)]
n = int(input())

for _ in range(n):
    ini_x, fin_x, ini_y, fin_y = map(int, input().split())
    for i in range(fin_y-ini_y):
        for j in range(fin_x-ini_x):
            xys[(ini_y+i)*101+ini_x+j] = "x"
ans = xys.count("x")
print(ans)
