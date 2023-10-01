#!/usr/bin/env python3
# わがらん
n = int(input())
c = [[] for _ in range(n)]

for i in range(n):
    x, y = map(int, input().split())
    c[x-1].append(y)
    c[y-1].append(x)

max_li = [max(li) for li in c]
maxf = max(max_li)

# def floor(num, li, maxf):
#     if li[num] != []:
#         for i in range(len(li[num])):
#             if maxf < li[num][i]:
#                 return li[num][i]
#             else:
#                 return maxf
#     else:
#         return maxf

# 行ける全てをループして最大値を保管する
for i in range(n):
    if c[i] != []:
        for j in range(len(c[i])):
            fff
