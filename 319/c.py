#!/usr/bin/env python3
import itertools

cells = [list(map(int, input().split())) for _ in range(3)]

row_list = [
    [0, 1, 2],  # 上から1行目
    [3, 4, 5],  # 上から2行目
    [6, 7, 8],  # 上から3行目
    [0, 3, 6],  # 上から1列目
    [1, 4, 7],  # 上から2列目
    [2, 5, 8],  # 上から3列目
    [0, 4, 8],  # 左上から右下
    [2, 4, 6],  # 右上から左下
]
order = [i for i in range(9)]

cells = sum(cells, [])
not_disappoint = 0
all_way = 0
for perm in itertools.permutations(order):
    all_way += 1
    disappoint_flag = False
    for a, b, c in row_list:
        if (
            (cells[a] == cells[b] and perm[a] < perm[c] and perm[b] < perm[c])
            or (cells[a] == cells[c] and perm[a] < perm[b] and perm[c] < perm[b])
            or (cells[b] == cells[c] and perm[b] < perm[a] and perm[c] < perm[a])
        ):
            disappoint_flag = True
    if not disappoint_flag:
        not_disappoint += 1

probability = not_disappoint / all_way
print(probability)
