#!/usr/bin/env python3

n = int(input())
s = str(input())

tmpl = ['RL', 'LR', 'UD', 'DU', 'RULD', 'ULDR', 'LDRU', 'DRUL', 'LURD', 'URDL', 'RDLU', 'DLUR', 'RRULLD', 'RULLDR', 'ULLDRR', 'LLDRRU', 'LDRRUL', 'DRRULL', ]
same = False
r_n, l_n, u_n, d_n = 0, 0, 0, 0
# 先頭から順に
for w in s:
    if w =='R':
        r_n += 1
    elif w == 'L':
        l_n += 1
    elif w == 'U':
        u_n += 1
    elif w == 'D':
        d_n += 1
    if r_n == l_n:
        if u_n == d_n:
            same = True
            break


if same == False:
    for w in tmpl:
        if w in s:
            same = True
            break
if same == False:
    print('No')
else:
    print('Yes')