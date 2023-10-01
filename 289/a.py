#!/usr/bin/env python3

s = str(input())
in_0 = []
in_1 = []
for i in range(len(s)):
    if s[i] == "0":
        in_0.append(int(i))
    elif s[i] == "1":
        in_1.append(int(i))

for i in range(len(s)):
    if i in in_0:
        s = s[:i] + "1" + s[i+1:]
    elif i in in_1:
        s = s[:i] + "0" + s[i+1:]

print(s)