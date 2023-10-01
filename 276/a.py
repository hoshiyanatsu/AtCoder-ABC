#!/usr/bin/env python3
S = input()
num = -1
i = 1
for w in S:
    if w == 'a':
        num = i
    i += 1
print(num)