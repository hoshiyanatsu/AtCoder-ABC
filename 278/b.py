#!/usr/bin/env python3
# def time(H, M):
H, M = map(int, input().split())
M = "{:0>2}".format(M)

if ( 0 <= H < 6 or 9 < H < 16 ):
    print(H, int(M))
elif 5 < H < 10:
    print(10, 00)
elif 15 < H < 20:
    print(20, 00)
elif (20 <= H <= 23):
    if int(M[0]) <= 3:
        print(H, int(M))

    elif 19 < H < 23:
        print(H+1, 00)

    else:
        print(00,00)
