#!/usr/bin/env python3

n = int(input())
A = list(map(int, input().split()))

# nums = [i+1 for i in range(n)]
i = 1

for p in A:
    if p != -1 & i < p:
        A[p-1] = -1
    # if i == nums[i-1]:
        # nums[p-1] = -1
    i += 1

cnt = 0
ans = ''
for a in A:
    if a != -1:
        cnt += 1
        ans += str(a) + ' '
print(cnt)
print(ans)