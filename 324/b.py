def main(n:int):
    calc = n
    if n%3==0:
        while (calc%3==0):
            calc = calc/3
    if n%2==0:
        while (calc%2==0):
            calc = calc/2
    if calc==1:
        print("Yes")
    else:
        print("No")

if __name__=="__main__":
    n = int(input())
    main(n=n)