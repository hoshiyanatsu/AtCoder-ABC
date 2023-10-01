#!/usr/bin/env python3

t = int(input())
tests = []

for i in range(t):
    test_i = []
    n = int(input())
    a = input().split()
    for j in range(n):
        test_i.append(a[j])
    tests.append(test_i)

for i in range(t):
    counter = 0
    for j in range(len(tests[i])):
        if int(tests[i][j])%2==1:
            counter += 1
    print(counter)