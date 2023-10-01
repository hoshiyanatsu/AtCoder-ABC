#!/usr/bin/env python3
n = int(input())
ice = [0] * (2 * n)
flavor = -1
max_oishi = 0
max_index = -1
second_oishi = 0

for i in range(n):
    ice_flavor, oishi = map(int, input().split())
    ice[2 * i] = ice_flavor
    ice[2 * i + 1] = oishi
    if oishi > max_oishi:
        max_oishi = oishi
        flavor = ice_flavor
        max_index = i

del ice[2 * max_index]
del ice[2 * max_index]
answer = max_oishi

for i in range(n - 1):
    if ice[2 * i] == flavor:
        pre = max_oishi + ice[2 * i + 1] / 2
    else:
        pre = max_oishi + ice[2 * i + 1]
    if pre > answer:
        answer = pre
print(int(answer))
