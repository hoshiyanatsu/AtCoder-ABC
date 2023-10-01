#!/usr/bin/env python3
n = int(input())
a = list(map(int, input().split()))

a = sorted(a)

min = a[0]
for i in range(n - 1):
    if (min + 1) != a[i + 1]:
        print(min + 1)
        break
    else:
        min += 1
