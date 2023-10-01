#!/usr/bin/env python3

x = input().split()
n = int(x[0])
m = int(x[1])

s = []
t = []

counter = 0

for i in range(n):
    si = str(input())
    s.append(si)
for j in range(m):
    ti = str(input())
    t.append(ti)

for num in range(n):
    for t_num in range(m):
        if s[num].endswith(t[t_num]):
            counter += 1
            break
print(counter)

