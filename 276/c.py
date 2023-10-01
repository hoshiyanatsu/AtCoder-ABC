#!/usr/bin/env python3
# 時間オーバー
import itertools

n = int(input())
P = list(map(int, input().split()))

all_j = sorted(list(itertools.permutations(P)))

for k in range(len(all_j)):
    if list(all_j[k]) == P:
        print(*list(all_j[k-1]))
        break