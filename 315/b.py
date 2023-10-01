#!/usr/bin/env python3


m = int(input())
d = list(map(int, input().split()))


def sum_list(x: int, li=d):
    total = 0
    for i in range(x + 1):
        total += li[i]
    return total


left = -1
right = m
mannaka = (sum(d) + 1) / 2

while right - left > 1:
    mid = int(left + (right - left) / 2)

    if sum_list(x=mid) < mannaka:
        left = mid
    else:
        right = mid

a = left + 2
b = int(mannaka - sum_list(x=left))
print(a, b)
