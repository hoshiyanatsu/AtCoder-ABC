#!/usr/bin/env python3

n, d, p = map(int, input().split())
f = list(map(int, input().split()))

all_f = sum(f)
amari = n%d
if amari == 0:
    all_p = int(n/d)*p
else:
    all_p = (int(n/d)+1)*p

least = min(all_f, all_p)
print(f"all_f={all_f}, all_p={all_p}")
b_least = least
if least==all_f:
    f = sorted(f, reverse=True)
    for i in range(int(n/d)+1):
        b_least = least
        if d*(i+1)<n:
            least -= sum(f[d*i:d*(i+1)])
        else:
            least -= sum(f[i:])
        least += p
        if b_least < least:
            break
else:
    f = sorted(f, reverse=False)
    if amari != 0 and amari-1<n:
        least -= p
        least += sum(f[0:amari-1])
    for i in range(int(n/d)):
        b_least = least
        least -= p
        if amari+d*(i+1) < n:
            least += sum(f[amari+d*i:amari+d*(i+1)])
        else:
            least += sum(f[amari+d*i:])
        if b_least < least:
            break
        print(f"b_least={b_least}, least={least}")

print(b_least)
