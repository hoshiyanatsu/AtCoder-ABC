#!/usr/bin/env python3

S = input()
nums = '0123456789'
alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

check = True
if len(S) != 8:
    check = False
else:
    if S[0] not in alph:
        check = False
    for i in range(1, 7):
        if i == 1 and S[i] == '0':
            check = False
        elif S[i] not in nums:
            check = False
            break
    if S[7] not in alph:
        check = False
if check:
    print("Yes")
else:
    print("No")