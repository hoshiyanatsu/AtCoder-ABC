#!/usr/bin/env python3

n, p, m = map(int, input().split())
mangetsu = p
count = 0
while mangetsu < n+1:
    count += 1
    mangetsu += m
print(count)