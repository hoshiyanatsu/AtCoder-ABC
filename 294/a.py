#!/usr/bin/env python3

n = int(input())
A = list(map(int, input().split()))

for i in A:
    if i%2==0:
        print(i, end=" ")
    
print()