#!/usr/bin/env python3

s = input()
n = int(len(s))
ans = ''
for i in range(int(n/2)):
    a = s[2*i+1]
    b = s[2*i]
    ans += a+b
print(ans)
