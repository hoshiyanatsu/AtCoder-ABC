#!/usr/bin/env python3

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
queries = []
for i in range(Q):
    queries.append(list(map(int, input().split())))

for i in range(Q):
    if queries[i][0] == 1:
        A[queries[i][1]-1] = queries[i][2]
    else:
        print(A[queries[i][1]-1])
    