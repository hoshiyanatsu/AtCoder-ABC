#!/usr/bin/env python3

N = input()
S = input()

gokaku = False
if 'o' in S and 'x' not in S:
    gokaku = True
if gokaku:
    print('Yes')
else:
    print('No')