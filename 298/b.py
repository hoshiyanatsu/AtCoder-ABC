#!/usr/bin/env python3
N = int(input())
 
A = ['' for _ in range(N)]
B = ['' for _ in range(N)]

for i in range(N):
    A[i] = list(map(int, input().split()))
for i in range(N):
    B[i] = list(map(int, input().split()))

kekka = False
a1_counter = 0
b1_counter = 0
b2_counter = 0
b3_counter = 0
b4_counter = 0
for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            a1_counter += 1
            if B[i][j] == 1:
                b1_counter += 1
            if B[N-1 - j][i] == 1:
                b2_counter += 1
            if B[N-1 - i][N-1 - j] == 1:
                b3_counter += 1
            if B[j][N-1 - i] == 1:
                b4_counter += 1
if a1_counter == b1_counter or a1_counter == b2_counter or a1_counter == b3_counter or a1_counter == b4_counter:
    kekka = True

if kekka:
    print('Yes')
else:
    print('No')