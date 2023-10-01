#!/usr/bin/env python3

N = int(input())
Q = int(input())
queries = [list(map(int, input().split())) for _ in range(Q)]

boxs = [[] for _ in range(N)]
nums = [[] for _ in range(2*(10**5))]
for i in range(Q):
    if queries[i][0] == 1:
        boxs[queries[i][2]-1].append(queries[i][1])
        nums[queries[i][1]-1].append(queries[i][2])
    elif queries[i][0] == 2:
        print(*sorted(boxs[queries[i][1]-1]))
    elif queries[i][0] == 3:
        print(*sorted(set(nums[queries[i][1]-1])))
        # x = queries[i][1]
        # for j in range(N):
        #     if x in boxs[j]:
        #         print(j + 1, end=" ")
        # print()