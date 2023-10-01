#!/usr/bin/env python3
N, M = map(int, input().split())
cities = [[] for _ in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    cities[u-1].append(v)
    cities[v-1].append(u)

for li in cities:
    li.sort()
    print(len(li), *li)