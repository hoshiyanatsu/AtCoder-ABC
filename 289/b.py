#!/usr/bin/env python3

N, M =map(int, input().split())
A = list(map(int, input().split()))
ans = []
l = 1

for i in range(N):
    if len(A) == 0:
        ans.append(i+1)
    else:
        if l > N:
            break
        r = l
        for k in range(len(A)+1):
            if r in A:
                r += 1
            else:
                for j in range(r-l+1):
                    ans.append(r-j)
                l = r+1

for i in ans:
    print(i, end=" ")
print()