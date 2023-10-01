#!/usr/bin/env python3

a, b = map(int, input().split())
if a % 3 == 0:
    print("No")
elif b - a == 1:
    print("Yes")
else:
    print("No")
