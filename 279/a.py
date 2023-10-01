#!/usr/bin/env python3
S = input()
count = 0
for i in S:
    if i == 'v':
        count += 1
    elif i == 'w':
        count += 2
print(count)