b = int(input())

a = 1
while a**a < b:
    a += 1

if a**a==b:
    print(a)
else:
    print(-1)