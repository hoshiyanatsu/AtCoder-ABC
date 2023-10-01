#!/usr/bin/env python3

n = int(input())
s = []
for i in range(n):
    si = input()
    s.append(si)

f = 0
for i in range(n):
    if s[i] == "For":
        f += 1

if f > n/2:
    print("Yes")
else:
    print("No")