#!/usr/bin/env python3

n, k = map(int, input().split())
s = list(input())

ctr = 0
for i in range(n):
    if s[i] == 'o' and ctr < k:
        ctr += 1
    else:
        s[i] = 'x'
print(''.join(s))