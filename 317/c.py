#!/usr/bin/env python3
import itertools

N, M = map(int, input().split())
roads = []
for _ in range(M):
    A, B, C = map(int, input().split())
    roads.append((A, B, C))

max_total = 0

# 全ての街の組み合わせに対して探索
for towns in itertools.permutations(range(1, N + 1)):
    total = 0
    visited = set()
    for i in range(N - 1):
        A, B, C = towns[i], towns[i + 1], 0
        for road in roads:
            if (road[0] == A and road[1] == B) or (road[0] == B and road[1] == A):
                C = road[2]
                break
        if C == 0:
            break
        total += C
        visited.add(A)
    else:
        visited.add(towns[N - 1])
        if len(visited) == N:
            max_total = max(max_total, total)

print(max_total)
