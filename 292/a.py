#!/usr/bin/env python3
s = str(input())
Omoji = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P' ,'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
i = 0
for w in s:
    i += 1
    if w in Omoji:
        print(i)
        break