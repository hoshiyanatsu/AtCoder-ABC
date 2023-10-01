#!/usr/bin/env python3
n, m = map(int, input().split())
cities = [set() for _ in range(1, n+2)]
abc = [list(map(int, input().split())) for _ in range(m)]


for a, b, c in abc:
    cities[a].add(b)
    cities[b].add(a)
print(cities)