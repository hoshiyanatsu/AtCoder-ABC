#!/usr/bin/env python3
n = int(input())
divided = [i for i in range(1, 10) if n % i == 0]

for i in range(n + 1):
    s = "-"
    for j in divided:
        if (n % j == 0) and (i % (n / j) == 0):
            s = j
            break
    print(s, end="")
print()
